import joblib
import streamlit as st

from config import MODEL_CONFIGS


"""Model loading and caching functionality."""

    
def load_artifacts(model_name: str):
        """
        Load model, feature names, and run summary.
        
        Args:
            model_name: Name of the model to load
            
        Returns:
            Tuple of (model, feature_names, run_summary)
            
        Raises:
            FileNotFoundError: If model files don't exist
            ValueError: If model_name is invalid
        """
        config = MODEL_CONFIGS.get(model_name)
        if not config:
            raise ValueError(f"Unknown model: {model_name}")
        
        try:
            # Load model
            model_path = config["model_file"]
            model = joblib.load(model_path)
            
            # Load feature names
            features_path = config["features_file"]
            feature_names = joblib.load(features_path)

            #load threshhold
            threshold_path = config["threshold_file"]

            feature_importance = None
            if not model_name == "Logistic Regression":
                  feature_importance = joblib.load(config["importance"])
            # Load summary
            return model, feature_names, (threshold_path, model_name, feature_importance)
        except FileNotFoundError as e:
            raise FileNotFoundError(
                f"Model files for '{model_name}' not found in {model_path}. " # pyright: ignore[reportPossiblyUnboundVariable]
                f"Please ensure all files exist. Error: {str(e)}"
            )
    
def get_available_models():
        """Get list of available model names."""
        return list(MODEL_CONFIGS.keys())
    
def get_model_config(model_name: str):
        """Get configuration for a specific model."""
        return MODEL_CONFIGS.get(model_name, {})




