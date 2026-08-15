"""Visualization functions for the fraud detection app."""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def create_fraud_gauge(fraud_probability: float, threshold: float) -> go.Figure:
    """
    Create a gauge chart for fraud probability.
    
    Args:
        fraud_probability: Fraud probability (0-1)
        threshold: Classification threshold
        
    Returns:
        Plotly Figure
    """
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=fraud_probability * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Fraud Risk Score", 'font': {'size': 24}},
        delta={
            'reference': threshold * 100,
            'relative': False,
            'valueformat': '.1f',
            'suffix': '%'
        },
        gauge={
            'axis': {
                'range': [0, 100],
                'tickwidth': 1,
                'tickcolor': "darkblue"
            },
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 33], 'color': '#51cf66'},
                {'range': [33, 66], 'color': '#fcc419'},
                {'range': [66, 100], 'color': '#ff6b6b'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': threshold * 100
            }
        }
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    return fig


def create_feature_importance_chart(feature_importance: pd.DataFrame, 
                                   top_n: int = 10) -> go.Figure:
    """
    Create a horizontal bar chart for feature importance.
    
    Args:
        feature_importance: DataFrame with 'Feature' and 'Importance' columns
        top_n: Number of top features to show
        
    Returns:
        Plotly Figure
    """
    top_features = feature_importance.head(top_n).sort_values('Importance')
    
    fig = go.Figure(go.Bar(
        x=top_features['Importance'],
        y=top_features['Feature'],
        orientation='h',
        marker_color='#4dabf7',
        hovertemplate='<b>%{y}</b><br>Importance: %{x:.2%}<extra></extra>'
    ))
    
    fig.update_layout(
        title=f"Top {top_n} Feature Importances",
        xaxis_title="Importance",
        yaxis_title="Feature",
        height=400,
        margin=dict(l=150, r=20, t=50, b=20)
    )
    
    return fig


def create_transaction_summary(input_data: dict) -> go.Figure:
    """
    Create a summary visualization of transaction data.
    
    Args:
        input_data: Dictionary with transaction data
        
    Returns:
        Plotly Figure
    """
    # Prepare data for visualization
    labels = ['Sender Before', 'Sender After', 'Recipient Before', 'Recipient After']
    values = [
        input_data['oldbalanceOrig'],
        input_data['newbalanceOrig'],
        input_data['oldbalanceDest'],
        input_data['newbalanceDest']
    ]
    colors = ['#4dabf7', '#74c0fc', '#69db7c', '#8ce99a']
    
    fig = go.Figure(go.Bar(
        x=labels,
        y=values,
        text=[f'${v:,.2f}' for v in values],
        textposition='outside',
        marker_color=colors,
        hovertemplate='<b>%{x}</b><br>Balance: $%{y:,.2f}<extra></extra>'
    ))
    
    # Add transaction amount annotation
    fig.add_annotation(
        x=0.5,
        y=max(values) * 1.1,
        text=f"Transaction Amount: ${input_data['amount']:,.2f}",
        showarrow=False,
        font=dict(size=14, color='darkblue')
    )
    
    fig.update_layout(
        title="Balance Overview",
        yaxis_title="Balance ($)",
        height=300,
        showlegend=False,
        bargap=0.3
    )
    
    return fig

def create_feature_contribution_chart(current_values: dict, 
                                     feature_importance: pd.DataFrame,
                                     top_n: int = 10) -> go.Figure:
    """
    Create a chart showing current feature values vs their importance.
    
    Args:
        current_values: Dictionary of current feature values
        feature_importance: DataFrame with 'Feature' and 'Importance' columns
        top_n: Number of top features to show
        
    Returns:
        Plotly Figure
    """
    if feature_importance is None or feature_importance.empty:
        fig = go.Figure()
        fig.add_annotation(
            text="No feature importance data available",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16)
        )
        fig.update_layout(height=400)
        return fig
    
    # Merge importance with current values
    top_features = feature_importance.head(top_n).copy()
    top_features['Current Value'] = top_features['Feature'].map(
        lambda x: current_values.get(x, 0)
    )
    
    # Create figure with dual axes
    fig = go.Figure()
    
    # Bars for importance
    fig.add_trace(go.Bar(
        x=top_features['Importance'],
        y=top_features['Feature'],
        orientation='h',
        name='Importance',
        marker_color='#4dabf7',
        text=[f'{v:.2%}' for v in top_features['Importance']],
        textposition='outside'
    ))
    
    # Add markers for current values
    fig.add_trace(go.Scatter(
        x=top_features['Current Value'] / top_features['Current Value'].max() if top_features['Current Value'].max() > 0 else [0]*len(top_features),
        y=top_features['Feature'],
        mode='markers',
        name='Current Value',
        marker=dict(
            size=12,
            color='#ff6b6b',
            symbol='star'
        ),
        text=[f'${v:,.2f}' if v > 100 else f'{v:.2f}' for v in top_features['Current Value']],
        hovertemplate='<b>%{y}</b><br>Current Value: %{text}<extra></extra>'
    ))
    
    fig.update_layout(
        title=f"Top {top_n} Features - Importance vs Current Value",
        xaxis_title="Importance / Normalized Value",
        yaxis_title="Feature",
        height=400,
        margin=dict(l=150, r=50, t=50, b=20),
        showlegend=True,
        barmode='group'
    )
    
    return fig