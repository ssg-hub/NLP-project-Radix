import plaidml.keras
import os

plaidml.keras.install_backend()

# Help MacOS be able to use Keras
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
# Gets rid of the processor warning.
os.environ['KMP_DUPLICATE_LIB_OK']='True'

