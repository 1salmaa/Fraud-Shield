"""Reusable Streamlit UI components."""

import streamlit as st
import pandas as pd
from typing import Optional, Tuple


def display_prediction_result(probability: float, threshold: float, is_fraud: bool):
    """
    Display prediction results with styling.
    
    Args:
        probability: Fraud probability (0-1)
        threshold: Classification threshold
        is_fraud: Binary prediction
    """
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Fraud Probability",
            f"{probability * 100:.2f}%",
            delta=f"{'Above' if probability >= threshold else 'Below'} Threshold"
        )
    
    with col2:
        st.metric(
            "Threshold",
            f"{threshold * 100:.2f}%",
            help="Transactions above this threshold are flagged as fraud"
        )
    
    with col3:
        status = "FRAUD" if is_fraud else "LEGITIMATE"
        st.metric(
            "Prediction Status",
            status,
            delta="Flagged" if is_fraud else "Cleared"
        )
    
    # Alert box
    if is_fraud:
        st.markdown("""
            <div style="background-color:#ff6b6b;padding:20px;border-radius:10px;
                        color:white;text-align:center;font-weight:bold;font-size:18px;">
                 HIGH RISK TRANSACTION DETECTED! This transaction has been flagged for review.
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="background-color:#51cf66;padding:20px;border-radius:10px;
                        color:white;text-align:center;font-weight:bold;font-size:18px;">
                 This transaction appears legitimate. No fraud indicators detected.
            </div>
        """, unsafe_allow_html=True)


def display_validation_results(errors: list, warnings: list):
    """
    Display validation results.
    
    Args:
        errors: List of error messages
        warnings: List of warning messages
    """
    if errors:
        st.error("Input validation failed:")
        for error in errors:
            st.error(f"- {error}")
    
    if warnings:
        st.warning("Validation Warnings:")
        for warning in warnings:
            st.warning(f"- {warning}")



def create_sidebar(model_names: list, default_model: str = "XGBoost"):
    """
    Create the sidebar UI elements.
    
    Returns:
        selected_model
    """
    st.sidebar.header("Model Selection")
    
    selected_model = st.sidebar.selectbox(
        "Select Model",
        options=model_names,
        index=model_names.index(default_model) if default_model in model_names else 0,
        help="Choose which model to use for prediction"
    )
    return selected_model