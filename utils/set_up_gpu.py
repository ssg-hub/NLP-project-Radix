# With Keras
# https://medium.com/@chris_birch/using-the-gpu-on-a-2018-macbook-pro-for-machine-learning-dc0735f500b1

import plaidml.keras
import os

plaidml.keras.install_backend()

# Help MacOS be able to use Keras
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
# Gets rid of the processor warning.
os.environ['KMP_DUPLICATE_LIB_OK']='True'

