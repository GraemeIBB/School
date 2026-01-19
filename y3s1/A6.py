
import cv2
import numpy as np
import matplotlib.pyplot as plt
def zero_crossing(img):
    zc = np.zeros(img.shape, dtype=np.uint8)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            patch = img[i - 1 : i + 2, j - 1 : j + 2]
            if patch.min() < 0 and patch.max() > 0:
                zc[i, j] = 255
    return zc
def plot_image(image, title=""):
    plt.imshow(image, cmap="gray", vmin=0, vmax=255)
    plt.axis("off")
    plt.title(title)
    plt.show()
def plot_intensity_profile(I):
    plt.figure()
    plt.plot(I[19, :])
    plt.title("Intensity Profile")
    plt.xlabel("Column")
    plt.ylabel("Intensity")
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    # Create test image with ramp edge
    size = 256
    ramp_width = 50
    I = np.zeros((size, size), dtype=np.float32)

    center = size // 2
    ramp_start = center - ramp_width // 2
    ramp_end = center + ramp_width // 2

    # Create ramp edge
    for i in range(size):
        if i < ramp_start:
            I[:, i] = 0
        elif i >= ramp_end:
            I[:, i] = 255
        else:
            # Linear ramp
            I[:, i] = 255 * (i - ramp_start) / ramp_width

    # Select horizontal line through middle
    middle_row = size // 2
    intensity_profile = I[middle_row, :]

    # Compute first derivative
    first_derivative = np.gradient(intensity_profile)

    # Apply Gaussian blur before second derivative
    sigma = 2.0
    I_blurred = cv2.GaussianBlur(I, (0, 0), sigma)
    blurred_profile = I_blurred[middle_row, :]

    # Compute second derivative on blurred profile
    second_derivative = np.gradient(np.gradient(blurred_profile))

    # Create plots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Plot 1: Original image with ramp edge
    axes[0, 0].imshow(I, cmap='gray', vmin=0, vmax=255)
    axes[0, 0].set_title('Test Image with Ramp Edge')
    axes[0, 0].axhline(y=middle_row, color='r', linestyle='--', linewidth=1, label='Sample line')
    axes[0, 0].legend()
    axes[0, 0].axis('off')

    # Plot 2: Intensity profile
    x = np.arange(len(intensity_profile))
    axes[0, 1].plot(x, intensity_profile, 'b-', linewidth=2)
    axes[0, 1].set_title('Intensity Profile (Horizontal Line)')
    axes[0, 1].set_xlabel('Pixel Position')
    axes[0, 1].set_ylabel('Intensity')
    axes[0, 1].grid(True, alpha=0.3)

    # Plot 3: First derivative
    axes[1, 0].plot(x, first_derivative, 'g-', linewidth=2)
    axes[1, 0].set_title('First Derivative of Intensity')
    axes[1, 0].set_xlabel('Pixel Position')
    axes[1, 0].set_ylabel('dI/dx')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(y=0, color='k', linestyle='-', linewidth=0.5)

    # Plot 4: Second derivative (from blurred image)
    axes[1, 1].plot(x, second_derivative, 'r-', linewidth=2)
    axes[1, 1].set_title(f'Second Derivative (Gaussian blur σ={sigma})')
    axes[1, 1].set_xlabel('Pixel Position')
    axes[1, 1].set_ylabel('d²I/dx²')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].axhline(y=0, color='k', linestyle='-', linewidth=0.5)

    plt.tight_layout()
    plt.show()

    print("Analysis complete!")
    print(f"Image size: {I.shape}")
    print(f"Intensity range: [{I.min():.1f}, {I.max():.1f}]")
    print(f"Max first derivative: {np.max(np.abs(first_derivative)):.2f}")
    print(f"Max second derivative: {np.max(np.abs(second_derivative)):.2f}")
