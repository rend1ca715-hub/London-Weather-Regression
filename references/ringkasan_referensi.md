## Regression Evaluation Metric

The regression model is evaluated using Mean Absolute Error (MAE), Mean Squared Error (MSE), and the Coefficient of Determination (R²).

### Scientific Evidence

According to Ocampo Osorio et al. (2024), regression model performance can be assessed using several evaluation metrics. The interpretation of these metrics differs depending on their mathematical properties.

The paper provides the following explanation:

 "Unlike classification metrics, proximity to 0 denotes better performance, except for R² for which higher values indicate better performance."

This statement supports the interpretation that lower MAE and MSE values indicate better predictive performance, while a higher R² value generally indicates a better model fit.

### Interpretation of the Metrics

- Mean Absolute Error (MAE):** Measures the average absolute difference between actual and predicted values. A value closer to 0 indicates smaller prediction errors.
- Mean Squared Error (MSE):** Measures the average squared difference between actual and predicted values. A value closer to 0 indicates smaller prediction errors, with larger errors receiving greater penalties.
- Coefficient of Determination (R²):** Measures how well the model explains the variation in the target variable. A value closer to 1 generally indicates better predictive performance. However, R² can also be negative.

### Conclusion

MAE, MSE, and R² are important metrics for evaluating regression model performance. Lower MAE and MSE values indicate smaller prediction errors, while an R² value closer to 1 generally indicates that the model explains a larger proportion of the variation in the target variable. Therefore, a good regression model is expected to achieve low MAE and MSE values and a high R² value. However, the evaluation results should also be interpreted based on the target variable's scale and the model's performance on unseen data.

### Reference

Ocampo Osorio, F., Alzate-Ricaurte, S., Mejia Vallecilla, T. E., & Cruz-Suarez, G. A. (2024). The anesthesiologist's guide to critically assessing machine
learning research: A narrative review. *BMC Anesthesiology, 24*, Article 452.

https://doi.org/10.1186/s12871-024-02840-y