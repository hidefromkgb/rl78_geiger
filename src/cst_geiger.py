import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider



alphas = [
    1,      # 00
    1,      # 01
    1 / 2,  # 02
    1 / 3,  # 03
    1 / 4,  # 04
    1 / 5,  # 05
    1 / 6,  # 06
    1 / 7,  # 07
    1 / 8,  # 08
    1 / 9,  # 09
    1 / 10, # 10
    1 / 11, # 11
    1 / 12, # 12
    1 / 13, # 13
    1 / 14, # 14
    1 / 15, # 15
    1 / 16, # 16
    1 / 16, # 17
    1 / 16, # 18
    1 / 16, # 19
    1 / 16, # 20
    1 / 16, # 21
    1 / 16, # 22
    1 / 16, # 23
    1 / 16, # 24
    1 / 16, # 25
    1 / 16, # 26
    1 / 16, # 27
    1 / 16, # 28
    1 / 16, # 29
    1 / 16, # 30
    1 / 16, # 31
    1 / 16, # 32
    1 / 16, # 33
    1 / 16, # 34
    1 / 16, # 35
    1 / 16, # 36
    1 / 16, # 37
    1 / 16, # 38
    1 / 16, # 39
    1 / 16, # 40
    1 / 16, # 41
    1 / 16, # 42
    1 / 16, # 43
    1 / 16, # 44
    1 / 16, # 45
    1 / 16, # 46
    1 / 16, # 47
    1 / 16, # 48
    1 / 16, # 49
    1 / 16, # 50
    1 / 16, # 51
    1 / 16, # 52
    1 / 16, # 53
    1 / 16, # 54
    1 / 16, # 55
    1 / 16, # 56
    1 / 16, # 57
    1 / 16, # 58
    1 / 16, # 59
    1 / 16, # 60
    1 / 16, # 61
    1 / 16, # 62
    1 / 16, # 63
    1 / 16,
]

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
    np.full(120, 0.5),
    np.full(120, 0.3),
    np.full(360, 0.1),
))

ref_array = (np.float64(ref_array) - 75) / 40

src_array = np.zeros(len(ref_array), dtype=int)

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

def cst_mcu(array, t_a = 0x0100):
    size_max = 64 # keep this value at 64 or lower

    event_buf = np.zeros(size_max, dtype=int)
    event_idx = 0 # starting value doesn't matter, safe to skip initialization
    output = []

    event_sum_curr = 0 # min: 0, max: 8191
    size_curr = size_max // 2
    for event_sum_next in array:
        size_next = size_curr + 1
        event_buf[event_idx % size_max] = event_sum_next
        esn = event_sum_next - event_sum_curr
        esp = event_sum_next + event_sum_curr
        for n in range(event_idx - 1, event_idx - size_curr, -1):
            event_sum_next = event_buf[n % size_max]
            esn += event_sum_next - event_sum_curr # min: -8191*64, max: 8191*64
            esp += event_sum_next + event_sum_curr # min: 0, max: (8191+8191)*64
            size_next -= esn**2 > ((t_a * esp) >> 8)
        output += [event_sum_curr + esn / size_curr]
        event_sum_curr += esn // size_curr
        size_curr = min(size_next, size_max)
        event_idx += 1

    return output

def cst_mcu_sc(array, t_a = 0x0100):
    size_max = 64 # keep this value at 64 or lower

    event_buf = np.zeros(size_max, dtype=int)
    event_idx = 0 # starting value doesn't matter, safe to skip initialization
    output = [[], []]

    event_sum_curr = 0 # min: 0, max: 8191
    size_curr = size_max // 2
    for event_sum_next in array:
        size_next = size_curr + 1
        event_buf[event_idx % size_max] = event_sum_next
        esn = event_sum_next - event_sum_curr
        esp = event_sum_next + event_sum_curr
        for n in range(event_idx - 1, event_idx - size_curr, -1):
            event_sum_next = event_buf[n % size_max]
            esn += event_sum_next - event_sum_curr # min: -8191*64, max: 8191*64
            esp += event_sum_next + event_sum_curr # min: 0, max: (8191+8191)*64
            size_next -= esn**2 > ((t_a * esp) >> 8)
        output[0] += [event_sum_curr + esn / size_curr]
        output[1] += [size_curr]
        event_sum_curr += esn // size_curr
        size_curr = min(size_next, size_max)
        event_idx += 1

    return output

# Simple moving average
def sma(array, window_size = 64):
    input_size = len(array)
    output = []

    window = np.zeros(window_size)
    total = 0
    for i, e in enumerate(array):
        total += e - window[i % window_size]
        window[i % window_size] = e
        output += [total / window_size]

    return output

# Exponential moving average
def ema(array, window_size = 64, alpha = None):
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
def rc_filter(array, tau = 8):
    alpha = 1 / (tau + 1)  # The actual formula is alpha = dt / (rc + dt) but the 1-second timestep simplifies things. Also tau = RC
    output = []
    last = 0
    for value in array:
        last = alpha * (value - last) + last
        output += [last]

    return output

def rc_filter_sc(array):
    global alphas
    output = []
    last = 0
    for value in zip(array[0], array[1]):
        last = alphas[value[1]] * (value[0] - last) + last
        output += [last]

    return output

# SMA with adaptive window size
# Source: https://habr.com/ru/articles/732456/
def sma_adaptive(array):
    max_windowsize=64
    target_counts = 500
    max_inter_rate = 500
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
            if (window_sum * iterations >= max_inter_rate): break
            if (window_sum >= target_counts): break
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

def cst_plus_func(array, func, min_alpha, max_alpha):
    peak_share = 0.25
    window_size = 64
    window = np.full(window_size, 1.0 / peak_share)

    c = cst_mcu(array)
    k = func(c)
    output = []

    total = window_size / peak_share
    for i, e in enumerate(array):
        total += e - window[i % window_size]
        window[i % window_size] = e
        alpha = 1 - min(peak_share * total / window_size, 1)
        alpha = min_alpha + alpha * (max_alpha - min_alpha)
        output += [k[i] * alpha + c[i] * (1 - alpha)]

    return output

# =============================================================================
# Post-filter algorithms applied on top of cst_mcu output
# =============================================================================

# Post-filter 1: Median-of-3 + adaptive RC cascade
# Stage 1 removes single-sample Poisson spikes (MCU cost: 3 comparisons).
# Stage 2 is the same adaptive RC as rc_filter_sc but on cleaner input.
def post_median3_rc(cst_output):
    """Median-of-3 spike removal followed by CST-adaptive RC smoothing."""
    global alphas
    values = cst_output[0]
    sizes = cst_output[1]
    n = len(values)

    # Stage 1: causal median-of-3 (current + 2 previous samples)
    med = []
    for i in range(n):
        if i < 2:
            med.append(values[i])
        else:
            a, b, c = values[i-2], values[i-1], values[i]
            med.append(a + b + c - min(a, b, c) - max(a, b, c))

    # Stage 2: adaptive RC using CST window size (same as rc_filter_sc)
    output = []
    last = 0.0
    for i in range(n):
        alpha = alphas[sizes[i]]
        last = alpha * (med[i] - last) + last
        output.append(last)

    return output

# Post-filter 2: Second-order (cascaded) adaptive RC
# Two first-order RC stages in series give a second-order roll-off
# (-40 dB/decade vs -20 dB/decade), much better noise rejection in
# steady-state while preserving the same transient response via the
# CST-adaptive alpha. MCU cost: 2 multiplies + 2 adds per sample.
def post_rc2_cascade(cst_output):
    """Two-stage cascaded adaptive RC filter (second-order IIR)."""
    global alphas
    values = cst_output[0]
    sizes = cst_output[1]
    n = len(values)

    output = []
    stage1 = 0.0
    stage2 = 0.0
    for i in range(n):
        alpha = alphas[sizes[i]]
        stage1 = alpha * (values[i] - stage1) + stage1
        stage2 = alpha * (stage1 - stage2) + stage2
        output.append(stage2)

    return output

# Post-filter 3: Alpha-beta tracker with CST-adaptive gains
# Uses the CST window size to modulate the alpha-beta gains:
# small window (transient) -> high alpha/beta for fast tracking;
# large window (steady) -> low alpha/beta for aggressive smoothing.
# The velocity term lets it track linear ramps with less lag than
# any pure averaging filter. MCU cost: ~4 multiplies per sample.
def post_alphabeta_adaptive(cst_output):
    """Alpha-beta predictor with CST-adaptive gain scheduling."""
    values = cst_output[0]
    sizes = cst_output[1]
    n = len(values)
    size_max = 64
    dt = 1.0

    # Gain bounds: [transient, steady-state]
    alpha_max = 0.8   # fast tracking during transients
    alpha_min = 0.06  # heavy smoothing during steady state
    beta_max = 0.05   # allow velocity updates during transients
    beta_min = 0.002  # suppress ringing during steady state

    output = []
    x_k = 0.0  # position (rate estimate)
    v_k = 0.0  # velocity (rate-of-change estimate)

    for i in range(n):
        # Map CST window size [1..size_max] -> gain interpolation [1..0]
        # Small window = high gain fraction, large window = low gain fraction
        w = sizes[i]
        frac = 1.0 - (w - 1) / (size_max - 1)  # 1.0 at w=1, 0.0 at w=64

        alpha = alpha_min + frac * (alpha_max - alpha_min)
        beta = beta_min + frac * (beta_max - beta_min)

        # Predict
        x_pred = x_k + v_k * dt

        # Update
        residual = values[i] - x_pred
        x_k = x_pred + alpha * residual
        v_k = v_k + (beta * residual) / dt

        if x_k < 0:
            x_k = 0.0

        output.append(x_k)

    return output


def dump(array):
    for i, n in enumerate(array):
        print('%04X%c' % (n, ' ' if (i + 1) % 8 else '\n'), end = '')

def refresh(regen):
    global alphas
    global src_array
    if (regen):
        seed = int(np.random.rand() * (2**32 - 1))
        np.random.seed(seed)
        plt.title('Filter comparison (seed = %d)' % (seed))

        trials = 10000 # Bernoulli trials per element (1 second)
        src_array = np.zeros(len(ref_array), dtype=int)
        norm_array = ref_array / trials
        for j in range(trials):
            src_array += np.random.random(len(ref_array)) < norm_array

    cst_array_sc = cst_mcu_sc(src_array)
    cst_array = cst_array_sc[0]

    if 'a' in plots: plots['a'][0].set_ydata(src_array)
    if 'b' in plots: plots['b'][0].set_ydata(cst_array_sc[1])
    if 'c' in plots: plots['c'][0].set_ydata(cst_array)
    if 'd' in plots: plots['d'][0].set_ydata(rc_filter_sc(cst_array_sc))
    if 'e' in plots: plots['e'][0].set_ydata(rc_filter(cst_array, 3))
    if 'f' in plots: plots['f'][0].set_ydata(rc_filter(cst_array, 6))
    if 'g' in plots: plots['g'][0].set_ydata(rc_filter(cst_array, 9))
    if 'h' in plots: plots['h'][0].set_ydata(rc_filter(cst_array, 12))
    if 'i' in plots: plots['i'][0].set_ydata(rc_filter(cst_array, 15))
    if 'p1' in plots: plots['p1'][0].set_ydata(post_median3_rc(cst_array_sc))
    if 'p2' in plots: plots['p2'][0].set_ydata(post_rc2_cascade(cst_array_sc))
    if 'p3' in plots: plots['p3'][0].set_ydata(post_alphabeta_adaptive(cst_array_sc))

    fig.canvas.draw()
    fig.canvas.flush_events()

def on_press(event):
    if event.key == ' ':
        refresh(True)

def update_alphas(i, val):
    global alphas
    alphas[i] = 1 / val
    refresh(False)

color_idx = 0

def pick_color():
    colors = ('#6000FF', '#FF0080', '#0080FF', '#FF5000', '#00FFB0', '#FFA000', '#50D000', '#D0D000')
    global color_idx
    color_idx += 1
    return colors[(color_idx - 1) % len(colors)]

# Plot data
fig, ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event', on_press)

plots = {
    'a': ax.plot(ref_array, linestyle='-', color='#C0C0C0', label = 'Raw data'),
    '.': ax.plot(ref_array, linestyle='-', color='#000000', label = 'Reference'),
    'c': ax.plot(ref_array, linestyle='-', color='#808080', label = 'CST (raw)', linewidth=0.8),
    'd': ax.plot(ref_array, linestyle='-', color=pick_color(), label = 'CST+RC(sc)'),
    'p1': ax.plot(ref_array, linestyle='-', color=pick_color(), label = 'CST+Med3+RC'),
    'p2': ax.plot(ref_array, linestyle='-', color=pick_color(), label = 'CST+RC2cas'),
    'p3': ax.plot(ref_array, linestyle='--', color=pick_color(), label = 'CST+AB(adp)'),
}

mul = 2
xt = plt.gca().get_xticks()
xt = np.arange(0, len(ref_array), (xt[1] - xt[0] if len(xt) > 1 else 200) / mul)
plt.xticks(xt, xt * mul)

refresh(True)

plt.xlabel('Seconds')
plt.ylabel('CP2S')
plt.grid(True)
plt.legend()

axes = []
sliders = []
for y in range(8):
    for x in range(8):
        axes += [fig.add_axes(
                [1 - (7-x)/128, 1/64 + 0.125 * (7-y), 1/128, 0.125 - 1/64])]
        sliders += [Slider(ax = axes[8 * y + x], label = "",
                           valstep = 1, valmin = 1, valmax = 16,
                           valinit = 1 / alphas[8 * y + x],
                           orientation = "vertical")]
        sliders[8 * y + x].on_changed(lambda val, i = 8 * y + x: update_alphas(i, val))

plt.show()