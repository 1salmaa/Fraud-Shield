from typing import Tuple, List, Optional, Dict

from config import FRAUD_CAPABLE_TYPES
"""Input validation for transaction data."""
    
def validate(txn_type: str, amount: float,
                 old_orig: float, new_orig: float,
                 old_dest: float, new_dest: float) -> Tuple[List[str], List[str]]:
        """
        Validate input data.
        
        Returns:
            Tuple of (errors, warnings)
        """
        errors = []
        warnings = []
        
        # Amount validation
        if amount <= 0:
            errors.append(
                "Amount must be greater than 0 — zero-amount transactions were removed "
                "during cleaning and the model has never seen one."
            )
        
        # Balance validation
        if old_orig < 0 or new_orig < 0 or old_dest < 0 or new_dest < 0:
            errors.append("All balances must be non-negative.")
        
        # Transaction type specific validation
        if txn_type == "CASH_IN":
            if new_orig < old_orig:
                warnings.append(
                    "Unusual for CASH_IN: the sender's balance normally increases "
                    "(they're depositing), but it went down here."
                )
        else:
            if new_orig > old_orig:
                warnings.append(
                    f"Unusual for {txn_type}: the sender's balance normally decreases "
                    "or stays the same, but it went up here."
                )
        
        # Zero balance pattern
        if amount > 0 and old_orig == 0 and new_orig == 0 and txn_type != "CASH_IN":
            warnings.append(
                "Sender balance is 0 both before and after a non-zero transaction — "
                "the model has seen this pattern (it's common in the fraud examples), "
                "but double check the balances are what you intended."
            )
        
        # Large amount warning
        if txn_type in FRAUD_CAPABLE_TYPES and amount > 1000000:
            warnings.append(
                f"Very large transaction amount (${amount:,.2f}) - this is unusual "
                f"and may warrant additional review."
            )
        
        # Consistency checks
        if abs(old_orig - new_orig) != amount and txn_type not in ["CASH_IN", "PAYMENT"]:
            # This is common in the data, but worth noting
            balance_diff = abs(old_orig - new_orig)
            warnings.append(
                f"Balance change (${balance_diff:,.2f}) doesn't match "
                f"transaction amount (${amount:,.2f}) — this may indicate "
                "additional fees, interest, or data recording issues."
            )
        
        return errors, warnings
    
def sanitize(self, amount: float, old_orig: float, new_orig: float,
                 old_dest: float, new_dest: float):
        """
        Sanitize input values (round, etc.).
        
        Returns:
            Dictionary of sanitized values
        """
        return {
            "amount": round(amount, 2),
            "old_orig": round(old_orig, 2),
            "new_orig": round(new_orig, 2),
            "old_dest": round(old_dest, 2),
            "new_dest": round(new_dest, 2)
        }
