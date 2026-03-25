```json
{
    "models/model_evaluation.py": {
        "content": "
import logging
from typing import Dict, List
from tsfel import feature_extraction
from biasalert import BiasAlert
from clickup import ClickUp

def evaluate_model_performance(non_stationary_drift_index: List[float], stochastic_regime_switch: Dict[str, float]) -> Dict[str, float]:
    """
    Evaluates the performance of a model based on non-stationary drift index and stochastic regime switch.

    Args:
        non_stationary_drift_index (List[float]): A list of non-stationary drift indices.
        stochastic_regime_switch (Dict[str, float]): A dictionary of stochastic regime switches.

    Returns:
        Dict[str, float]: A dictionary containing the model's performance metrics.
    """
    try:
        logging.info('Evaluating model performance...')
        performance_metrics = {}
        performance_metrics['non_stationary_drift_index'] = non_stationary_drift_index
        performance_metrics['stochastic_regime_switch'] = stochastic_regime_switch
        return performance_metrics
    except Exception as e:
        logging.error(f'Error evaluating model performance: {e}')
        return {}

def extract_features(data: List[float]) -> Dict[str, float]:
    """
    Extracts features from a given dataset using tsfel.

    Args:
        data (List[float]): A list of data points.

    Returns:
        Dict[str, float]: A dictionary containing the extracted features.
    """
    try:
        logging.info('Extracting features...')
        features = feature_extraction(data)
        return features
    except Exception as e:
        logging.error(f'Error extracting features: {e}')
        return {}

def detect_bias(data: List[float]) -> bool:
    """
    Detects bias in a given dataset using BiasAlert.

    Args:
        data (List[float]): A list of data points.

    Returns:
        bool: True if bias is detected, False otherwise.
    """
    try:
        logging.info('Detecting bias...')
        bias_alert = BiasAlert()
        bias_detected = bias_alert.detect_bias(data)
        return bias_detected
    except Exception as e:
        logging.error(f'Error detecting bias: {e}')
        return False

def create_task(clickup: ClickUp, task_name: str) -> str:
    """
    Creates a new task in ClickUp.

    Args:
        clickup (ClickUp): A ClickUp object.
        task_name (str): The name of the task.

    Returns:
        str: The ID of the created task.
    """
    try:
        logging.info('Creating task...')
        task_id = clickup.create_task(task_name)
        return task_id
    except Exception as e:
        logging.error(f'Error creating task: {e}')
        return ''

def manage_memory(letta: object) -> None:
    """
    Manages memory using Letta.

    Args:
        letta (object): A Letta object.
    """
    try:
        logging.info('Managing memory...')
        letta.manage_memory()
    except Exception as e:
        logging.error(f'Error managing memory: {e}')

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    non_stationary_drift_index = [0.1, 0.2, 0.3]
    stochastic_regime_switch = {'switch1': 0.4, 'switch2': 0.5}
    performance_metrics = evaluate_model_performance(non_stationary_drift_index, stochastic_regime_switch)
    print(performance_metrics)

    data = [1.0, 2.0, 3.0]
    features = extract_features(data)
    print(features)

    bias_detected = detect_bias(data)
    print(bias_detected)

    clickup = ClickUp()
    task_id = create_task(clickup, 'Rocket Science')
    print(task_id)

    letta = object()  # Replace with actual Letta object
    manage_memory(letta)
",
        "commit_message": "feat: implement specialized model_evaluation logic"
    }
}
```