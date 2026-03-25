```json
{
    "utils/data_preprocessing.py": {
        "content": "
import logging
from typing import List, Dict
import numpy as np
from tsfel import feature_extraction
from tsfel.feature_extraction import features
from Bardeen import StateGraph
from Letta import MemoryManager

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_knitting_mill_features(data: List[Dict], non_stationary_drift_index: int) -> List[Dict]:
    """
    Extract features from knitting mill data.

    Args:
    - data (List[Dict]): Knitting mill data.
    - non_stationary_drift_index (int): Index of non-stationary drift.

    Returns:
    - List[Dict]: Extracted features.
    """
    try:
        # Initialize feature extractor
        extractor = feature_extraction.FeatureExtractor()
        
        # Extract features
        extracted_features = []
        for sample in data:
            features = extractor.extract_features(sample)
            extracted_features.append(features)
        
        # Apply non-stationary drift index
        extracted_features = [features[non_stationary_drift_index] for features in extracted_features]
        
        logger.info('Features extracted successfully')
        return extracted_features
    
    except Exception as e:
        logger.error(f'Error extracting features: {e}')
        return []

def stochastic_regime_switch(data: List[Dict], threshold: float) -> List[Dict]:
    """
    Apply stochastic regime switch to knitting mill data.

    Args:
    - data (List[Dict]): Knitting mill data.
    - threshold (float): Threshold for regime switch.

    Returns:
    - List[Dict]: Data with applied regime switch.
    """
    try:
        # Initialize memory manager
        memory_manager = MemoryManager()
        
        # Apply regime switch
        switched_data = []
        for sample in data:
            if sample['value'] > threshold:
                sample['regime'] = 'high'
            else:
                sample['regime'] = 'low'
            switched_data.append(sample)
        
        # Manage memory
        memory_manager.free_memory()
        
        logger.info('Regime switch applied successfully')
        return switched_data
    
    except Exception as e:
        logger.error(f'Error applying regime switch: {e}')
        return []

def create_state_graph(data: List[Dict]) -> StateGraph:
    """
    Create state graph from knitting mill data.

    Args:
    - data (List[Dict]): Knitting mill data.

    Returns:
    - StateGraph: Created state graph.
    """
    try:
        # Initialize state graph
        state_graph = StateGraph()
        
        # Add nodes and edges
        for sample in data:
            state_graph.add_node(sample['state'])
            state_graph.add_edge(sample['state'], sample['next_state'])
        
        logger.info('State graph created successfully')
        return state_graph
    
    except Exception as e:
        logger.error(f'Error creating state graph: {e}')
        return None

if __name__ == '__main__':
    # Simulate 'Rocket Science' problem
    data = [
        {'state': 'launch', 'next_state': 'orbit', 'value': 100},
        {'state': 'orbit', 'next_state': 're-entry', 'value': 50},
        {'state': 're-entry', 'next_state': 'landing', 'value': 20}
    ]
    
    # Extract features
    extracted_features = extract_knitting_mill_features(data, 1)
    print(extracted_features)
    
    # Apply regime switch
    switched_data = stochastic_regime_switch(data, 50)
    print(switched_data)
    
    # Create state graph
    state_graph = create_state_graph(data)
    print(state_graph)
",
        "commit_message": "feat: implement specialized data_preprocessing logic"
    }
}
```