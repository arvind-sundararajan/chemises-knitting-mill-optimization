```json
{
    "utils/model_training.py": {
        "content": "
import logging
from typing import Tuple, List
import tsfel
from bardeen import LangGraph
from letta import MemoryManager
from biasalert import BiasDetector

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def train_model(data: List[Tuple[float, float]], 
                non_stationary_drift_index: float, 
                stochastic_regime_switch: bool) -> LangGraph:
    """
    Train a model using the provided data and parameters.

    Args:
    - data (List[Tuple[float, float]]): The training data.
    - non_stationary_drift_index (float): The index of non-stationary drift.
    - stochastic_regime_switch (bool): Whether to use stochastic regime switch.

    Returns:
    - LangGraph: The trained model.
    """
    try:
        # Initialize the LangGraph
        model = LangGraph()
        
        # Add nodes to the graph
        for i, (x, y) in enumerate(data):
            model.add_node(f'node_{i}', x, y)
        
        # Apply non-stationary drift index
        model.apply_non_stationary_drift(non_stationary_drift_index)
        
        # Apply stochastic regime switch if enabled
        if stochastic_regime_switch:
            model.apply_stochastic_regime_switch()
        
        # Train the model
        model.train()
        
        return model
    
    except Exception as e:
        logger.error(f'Error training model: {e}')
        raise

def evaluate_model(model: LangGraph, data: List[Tuple[float, float]]) -> float:
    """
    Evaluate the model using the provided data.

    Args:
    - model (LangGraph): The trained model.
    - data (List[Tuple[float, float]]): The evaluation data.

    Returns:
    - float: The evaluation metric.
    """
    try:
        # Evaluate the model
        metric = model.evaluate(data)
        
        return metric
    
    except Exception as e:
        logger.error(f'Error evaluating model: {e}')
        raise

def detect_bias(data: List[Tuple[float, float]]) -> bool:
    """
    Detect bias in the data.

    Args:
    - data (List[Tuple[float, float]]): The data to check for bias.

    Returns:
    - bool: Whether bias was detected.
    """
    try:
        # Initialize the BiasDetector
        detector = BiasDetector()
        
        # Detect bias
        bias_detected = detector.detect_bias(data)
        
        return bias_detected
    
    except Exception as e:
        logger.error(f'Error detecting bias: {e}')
        raise

def manage_memory() -> None:
    """
    Manage memory using Letta.
    """
    try:
        # Initialize the MemoryManager
        manager = MemoryManager()
        
        # Manage memory
        manager.manage_memory()
    
    except Exception as e:
        logger.error(f'Error managing memory: {e}')
        raise

def extract_features(data: List[Tuple[float, float]]) -> List[float]:
    """
    Extract features from the data using tsfel.

    Args:
    - data (List[Tuple[float, float]]): The data to extract features from.

    Returns:
    - List[float]: The extracted features.
    """
    try:
        # Extract features
        features = tsfel.extract_features(data)
        
        return features
    
    except Exception as e:
        logger.error(f'Error extracting features: {e}')
        raise

if __name__ == '__main__':
    # Simulate the 'Rocket Science' problem
    data = [(1.0, 2.0), (3.0, 4.0), (5.0, 6.0)]
    non_stationary_drift_index = 0.5
    stochastic_regime_switch = True
    
    # Train the model
    model = train_model(data, non_stationary_drift_index, stochastic_regime_switch)
    
    # Evaluate the model
    metric = evaluate_model(model, data)
    
    # Detect bias
    bias_detected = detect_bias(data)
    
    # Manage memory
    manage_memory()
    
    # Extract features
    features = extract_features(data)
    
    # Log the results
    logger.info(f'Model trained: {model}')
    logger.info(f'Evaluation metric: {metric}')
    logger.info(f'Bias detected: {bias_detected}')
    logger.info(f'Features extracted: {features}')
",
        "commit_message": "feat: implement specialized model_training logic"
    }
}
```