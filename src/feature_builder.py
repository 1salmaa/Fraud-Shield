"""Feature building for model input."""
import pandas as pd

from config import TRANSACTION_TYPES


def set_feature_names(features: list):
     global feature_names
     feature_names = features

def get_feature_names():
     return feature_names
     
def build_row(step: int, txn_type: str, amount: float,
                  old_orig: float, new_orig: float, 
                  old_dest: float, new_dest: float):
        """
        Build a feature row for prediction.
        
        Args:
            step: Hour of transaction
            txn_type: Transaction type
            amount: Transaction amount
            old_orig: Sender's balance before
            new_orig: Sender's balance after
            old_dest: Recipient's balance before
            new_dest: Recipient's balance after
            
        Returns:
            DataFrame with features in the correct order
            
        Raises:
            ValueError: If required features are missing
        """
        # Calculate derived features
        error_balance_dest = old_dest + amount - new_dest
        
        # Base features
        row = {
            "step": step,
            "amount": amount,
            "oldbalanceOrig": old_orig,
            "newbalanceOrig": new_orig,
            "oldbalanceDest": old_dest,
            "newbalanceDest": new_dest,
            "errorBalanceDest": error_balance_dest,
        }
        
        # Add optional derived features if they exist
        derived_features = get_derived_features(
            step, amount, old_orig, new_orig, old_dest, new_dest
        )
        row.update(derived_features)
        
        # One-hot encode transaction type
        for t in TRANSACTION_TYPES:
            if t == txn_type:
                row[f"type_{t}"] = 1  
            else: row[f"type_{t}"] = 0
        
        # Validate all features are present
        missing = [name for name in feature_names if name not in row]
        if missing:
            raise ValueError(
                f"Missing expected features: {missing}. "
                f"Available features: {list(row.keys())}"
            )
        
        # Return DataFrame with correct column order
        return pd.DataFrame(
            [[row[name] for name in feature_names]], 
            columns=feature_names
        )
    
def get_derived_features(step: int, amount: float,
                              old_orig: float, new_orig: float,
                              old_dest: float, new_dest: float):
        """Calculate derived features that may be needed."""
        features = {}
        
        if "errorBalanceOrig" in get_feature_names():
            features["errorBalanceOrig"] = old_orig - new_orig - amount
        
        if "balanceChangeOrig" in get_feature_names():
            features["balanceChangeOrig"] = old_orig - new_orig
        
        if "balanceChangeDest" in get_feature_names():
            features["balanceChangeDest"] = new_dest - old_dest
        
        if "amountToOrigBalance" in get_feature_names():
            features["amountToOrigBalance"] = amount / (old_orig + 1) if (old_orig + 1) != 0 else 0
        
        if "amountToDestBalance" in get_feature_names():
            features["amountToDestBalance"] = amount / (old_dest + 1) if (old_dest + 1) != 0 else 0
        
        return features
    
def validate_features():
        """Get list of expected feature names."""
        return feature_names.copy()
