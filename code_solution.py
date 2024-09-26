def filter_image(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
  if image.shape[0] < kernel.shape[0] or image.shape[1] < kernel.shape[1]:
    raise ValueError
  else:
    result = np.zeros((image.shape[0] - kernel.shape[0] + 1, image.shape[1] - kernel.shape[0] + 1))
    for i in range(image.shape[0] - kernel.shape[0] + 1):
      for j in range(image.shape[1] - kernel.shape[1] + 1):
        result[i, j] = np.sum(image[i:i+kernel.shape[0], j:j + kernel.shape[1]] * kernel)
    return result
