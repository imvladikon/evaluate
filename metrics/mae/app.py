import evaluate
from evaluate.utils import launch_gradio_widget


module = evaluate.load("mae")
launch_gradio_widget(module)