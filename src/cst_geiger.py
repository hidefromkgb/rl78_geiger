import numpy as np
import matplotlib.pyplot as plt

# Centered significance test
# DOI: 10.1109/tns.2016.2601785
def cst(array):
    max_window_size = 64

    output = []
    event_buf = np.zeros(max_window_size, dtype=int)
    buf_head = 0
    lambda_cur = 0
    lambda_prev = 0
    sigma_cur = 0
    sigma_prev = 0

    l_t = int(max_window_size / 2)
    t_a = 1.0

    for idx, sample in enumerate(array):
        L = 0
        event_buf[buf_head] = sample
        buf_idx = buf_head
        event_sum = sample

        for i in range(1, l_t):
            buf_idx -= 1
            if buf_idx < 0:
                buf_idx = max_window_size - 1

            event_sum += event_buf[buf_idx]
            lambda_cur = event_sum / (i+1)
            sigma_cur = lambda_cur / (i+1)

            if ((lambda_cur - lambda_prev)**2) > (t_a**2 * (sigma_cur + sigma_prev)):
                L += 1

        l_t = l_t - L + 1
        lambda_prev = lambda_cur
        sigma_prev = sigma_cur
        buf_head += 1
        if buf_head >= max_window_size:
            buf_head = 0

        output.append(lambda_cur)

    return output

def cst_mcu(array):
    t_a = 0x0100 # for n in $(seq 0 4095); do printf "0x%04X " $n; echo "sqrt($n/256)" | bc -l; done
    size_max = 64 # keep this value at 64 or lower

    beta = 2

    event_buf = np.zeros(size_max, dtype=int)
    event_idx = 0 # starting value doesn't matter, safe to skip initialization
    output = []

    event_sum_curr = 0 # min: 0, max: 8191
    size_curr = size_max // 2
    for event_sum_next in array:
        event_sum_next += beta
        size_next = size_curr + 1
        event_buf[event_idx % size_max] = event_sum_next
        esn = event_sum_next - event_sum_curr
        esp = event_sum_next + event_sum_curr
        for n in range(event_idx - 1, event_idx - size_curr, -1):
            event_sum_next = event_buf[n % size_max]
            esn += event_sum_next - event_sum_curr # min: -8191*64, max: 8191*64
            esp += event_sum_next + event_sum_curr # min: 0, max: (8191+8191)*64
            size_next -= esn**2 > ((t_a * esp) >> 8)
        output += [event_sum_curr + esn / size_curr - beta]
        event_sum_curr += esn // size_curr
        size_curr = min(size_next, size_max)
        event_idx += 1

    return output

# Simple moving average
def sma(array, window_size=60):
    input_size = len(array)
    output = []

    for i in range(input_size):
        if i < window_size:
            window = array[0:i]
        else:
            window = array[i - window_size + 1:i]
        window_average = np.sum(window) / window_size
        output.append(window_average)

    return np.array(output)

# Exponential moving average
def ema(array, window_size=60, alpha=None):
    if alpha is None:
        alpha = 2 / (window_size + 1)
    alpha_array = []
    for i in range(window_size):
        alpha_array.append(np.power((1-alpha), i))

    alpha_sum = np.sum(alpha_array)

    input_size = len(array)
    output = []

    for i in range(input_size):
        if i < window_size:
            window = array[0:i]
        else:
            window = array[i - window_size + 1:i]

        exp_sum = 0

        for m, n in zip(reversed(window), alpha_array):
            exp_sum += m * n

        exp_avg = exp_sum / alpha_sum

        output.append(exp_avg)

    return np.array(output)

# RC filter with a given time constant
rc = 20  # RC time constant, seconds
def rc_filter(array, tau):
    alpha = 1 / (tau+1)  # The actual formula is alpha = dt / (rc + dt) but the 1-second timestep simplifies things. Also tau = RC
    output = [0]
    output[0] = alpha * array[0]
    for i in range(1, len(array)):
        output.append(alpha * array[i] + (1 - alpha) * output[i - 1])

    return output

# SMA with adaptive window size
# Source: https://habr.com/ru/articles/732456/
def sma_adaptive(array, target_counts=100, max_windowsize=120):
    thresh_delta = 30
    hi_thresh = 8
    lo_thresh = 0.125
    window_size = max_windowsize
    output = []

    for i in range(len(array)):
        window_sum = 0
        array_idx = i
        iterations = 0
        while (iterations < max_windowsize):
            iterations += 1
            window_sum += array[array_idx]
            array_idx -= 1

            if array_idx < 0: break   # reached end of the window
            #if window_sum >= target_counts: break

            if (window_sum >= target_counts) and (iterations >= 2): break  # counted over 100 counts and averaged at least 2 samples
            '''
            if i > 2:                 # abrupt change detect through difference
                if (abs(array[array_idx] - array[array_idx - 1]) > thresh_delta) and (abs(array[array_idx] - array[array_idx - 2]) > thresh_delta):
                    break
            '''
            if i > 2:         # abrupt change detect through ratio
                if (array[array_idx - 1] > 0) and (array[array_idx - 2] > 0):
                    prev1 = array[array_idx] / array[array_idx - 1]
                    prev2 = array[array_idx] / array[array_idx - 2]
                    isLarger = True if (prev1 >= hi_thresh) and (prev2 >= hi_thresh) else False
                    isSmaller = True if  (prev1 <= lo_thresh) and (prev2 <= lo_thresh) else False
                    if isLarger == True or isSmaller == True:
                        # return average of only last 2-4 samples?
                        break

        output.append(window_sum / iterations)

    return np.array(output)

# Adaptive tapped delay line FIR filter
# DOI: 10.1016/j.radmeas.2005.08.001
def fir_adaptive(array, method=1):
    assert (method == 1) or (method == 2), "fir_adaptive: method can only be 1 or 2"
    # The authors didn't specify FIR1 and FIR2 filter coefficients
    pass

def kalman(array):
    output = []
    Q = 0.04  # Process noise covariance, lower - smoother (def: 0.1)
    R = 5     # Measurement noise covariance, higher - smoother (def: 1.0)

    r_k = 0.5   # Initialize dose rate estimate
    P_k = 1.0 # Initialize error covariance

    for z_k in array:
        # Prediction step
        r_k_minus = r_k
        P_k_minus = P_k + Q

        # Update step
        K_k = P_k_minus / (P_k_minus + R)
        r_k = r_k_minus + K_k * (z_k - r_k_minus)
        P_k = (1 - K_k) * P_k_minus

        if (r_k < 0): r_k = 0
        output.append(r_k)

    return output

# Source: https://gist.github.com/balzer82/7f29431735306441b566
def alpha_beta(array):
    alpha = 0.25  # lower - smoother, def: 0.85
    beta = 0.001  # lower - more ringing suppression, def: 0.005
    dt = 1.0      # 1-second time step

    x_k = 0.0 # Initial position
    v_k = 0.0 # Initial velocity
    output = []

    for sample in array:
        x_k = x_k + v_k * dt
        r_k = sample - x_k
        x_k = x_k + alpha * r_k
        v_k = v_k + (beta * r_k) / dt
        if (x_k < 0): x_k = 0
        output.append(x_k)

    return output

# Generalized likelihood ratio
# DOI: 10.1016/j.nima.2008.06.050
def glr(array):
    # Based on SPRT but can actually smooth the data
    # Too complex for selected microcontroller
    pass

def kalman_x_cst(array):
    min_alpha = 0.125
    max_alpha = 1.0
    peak_share = 0.25
    window_size = 64
    window = np.full(window_size, 1.0 / peak_share)

    c = cst_mcu(array)
    k = kalman(c)
    output = []

    total = window_size / peak_share
    for i, e in enumerate(array):
        total += e - window[i % window_size]
        window[i % window_size] = e
        alpha = 1 - min(peak_share * total / window_size, 1)
        alpha = min_alpha + alpha * (max_alpha - min_alpha)
        output += [k[i] * alpha + c[i] * (1 - alpha)]

    return output



def dump(array):
    for i, n in enumerate(array):
        print('%04X%c' % (n, ' ' if (i + 1) % 8 else '\n'), end = '')

def refresh():
    seed = int(np.random.rand() * (2**32 - 1))
    #seed = 1628747943
    np.random.seed(seed)
    print(seed)
    plt.title('Filter comparison (seed = %d)' % (seed))

    # Generate synthetic radiation pulse data
    # DOI: 10.1109/LASCAS.2016.7451002
    trials = 10000 # Bernoulli trials per element (1 second)
    src_array = np.zeros(len(ref_array), dtype=int)
    norm_array = ref_array / trials
    for j in range(trials):
        src_array += np.random.random(len(ref_array)) < norm_array

    #dump(src_array)
    #print('---')
    #dump(np.int32(cst_mcu(src_array)))

    if 'a' in plots: plots['a'][0].set_ydata(src_array)
    if 'b' in plots: plots['b'][0].set_ydata(sma_adaptive(src_array))
    if 'c' in plots: plots['c'][0].set_ydata(sma(src_array))
    if 'd' in plots: plots['d'][0].set_ydata(ema(src_array))
    if 'e' in plots: plots['e'][0].set_ydata(rc_filter(cst_mcu(src_array), rc))
    if 'f' in plots: plots['f'][0].set_ydata(kalman(cst_mcu(src_array)))
    if 'F' in plots: plots['F'][0].set_ydata(kalman_x_cst(src_array))
    if 'g' in plots: plots['g'][0].set_ydata(alpha_beta(cst_mcu(src_array)))
    if 'h' in plots: plots['h'][0].set_ydata(cst(src_array))
    if 'i' in plots: plots['i'][0].set_ydata(cst_mcu(src_array))

    fig.canvas.draw()
    fig.canvas.flush_events()

def on_press(event):
    if event.key == ' ':
        refresh()

# Define the reference functions
ref_array = np.concatenate((
    np.full(120, 10),
    np.full(120, 5),
    np.full(120, 100),
    np.fromfunction(lambda i: 60 - 0.5 * i, (120,)),
    np.fromfunction(lambda i: 300/(np.sqrt(2 * np.pi)) * np.exp(-((i - 60)/15)**2 / 2), (120,)),
    np.fromfunction(lambda i: 300/(np.sqrt(2 * np.pi)) * np.exp(-((i - 60)/15)**2 / 2), (120,)),
    np.full(120, 0.33),
    np.full(120, 0.66),
    np.full(120, 0.99),
    np.fromfunction(lambda i: 20/(np.sqrt(2 * np.pi)) * np.exp(-((i - 60)/15)**2 / 2) + 0.99, (120,)),
    np.full(120, 0.99),
    np.full(120, 0.66),
    np.full(120, 0.33),
))

#ref_array += 8000

# Plot data
fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', on_press)
plots = {
    'a': ax.plot(ref_array, linestyle='-', color='#C0C0C0', label = 'Raw data'),
    '.': ax.plot(ref_array, linestyle='-', color='#000000', label = 'Reference'),
    #'b': ax.plot(ref_array, linestyle='-', color='#00C000', label = 'Adaptive SMA'),
    #'c': ax.plot(ref_array, linestyle='-', color='#0080FF', label = 'SMA'),
    #'d': ax.plot(ref_array, linestyle='-', color='#00FF00', label = 'EWMA'),
    #'e': ax.plot(ref_array, linestyle='-', color='#FF00FF', label = f'RC, τ={rc}s'),
    'f': ax.plot(ref_array, linestyle='-', color='#8080FF', label = 'Kalman × CST'),
    #'g': ax.plot(ref_array, linestyle='-', color='#FFC060', label = 'Alpha-beta'),
    #'h': ax.plot(ref_array, linestyle='-', color='#FF0000', label = 'CST'),
    'i': ax.plot(ref_array, linestyle='-', color='#FFC060', label = 'CST_optimized'),
    'F': ax.plot(ref_array, linestyle='-', color='#FF0000', label = 'CST + Kalman × CST'),
}

mul = 2
xt = plt.gca().get_xticks()
xt = np.arange(0, len(ref_array), (xt[1] - xt[0] if len(xt) > 1 else 200) / mul)
plt.xticks(xt, xt * mul)

refresh()

plt.xlabel('Seconds')
plt.ylabel('CP2S')
plt.grid(True)
plt.legend()
plt.show()
