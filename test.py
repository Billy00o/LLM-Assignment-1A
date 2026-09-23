from langchain_community.llms import LlamaCpp

# Load the model
llm = LlamaCpp(
    model_path="./models/Phi-4-mini-instruct-Q4_K_M.gguf",
    temperature=0.1,
    max_tokens=50,
    n_ctx=512,
    verbose=False
)

def test_llm_response():
    output = llm.invoke("What is the capital of France?")
    print("Model answer:", output)
    
    # Check if the answer contains "Paris"
    assert "Paris" in output, "Test failed: 'Paris' not found in the answer"
    print("Test passed!")

if __name__ == "__main__":
    test_llm_response()