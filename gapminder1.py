if __name__ == '__main__':

    # TODO: Add import statements
    import pandas as pd
    from sklearn.linear_model import LinearRegression

    # Assign the dataframe to this variable.
    # TODO: Load the data
    bmi_life_data = pd.read_csv("data_gapminder1.csv")

    # Make and fit the linear regression model
    # TODO: Fit the model and Assign it to bmi_life_model
    bmi_life_model = LinearRegression()
    bmi_life_model.fit(bmi_life_data[['BMI']], bmi_life_data[['Life expectancy']])

    # Mak a prediction using the model
    # TODO: Predict life expectancy for a BMI value of 21.07931

    # TODO: Seems there is a problem here
    laos_life_exp = bmi_life_model.predict(21.07931)