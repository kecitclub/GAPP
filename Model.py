from llama_cpp import Llama

class Model:
    def __init__(self):
        
        llm = Llama(
            model_path="C:\\Users\\achar\\Dristi-Hackathon\\unsloth.Q8_0.gguf"
            # n_gpu_layers=-1, # Uncomment to use GPU acceleration
            # seed=1337, # Uncomment to set a specific seed
            # n_ctx=2048, # Uncomment to increase the context window
        )

