import flask
import pandas as pd
from joblib import dump, load
from sklearn.preprocessing import LabelEncoder
import plotly.express as px

with open(f'model/model.pkl', 'rb') as f:
    model = load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return flask.render_template('main.html')

    if flask.request.method == 'POST':
        Country = flask.request.form['Country']
        Year = flask.request.form['Year']
        schizophrenia = flask.request.form['schizophrenia']
        bipolar = flask.request.form['bipolar']
        eating_disorder = flask.request.form['eating_disorder']
        anxiety = flask.request.form['anxiety']
        drug_use = flask.request.form['drug_use']
        depression = flask.request.form['depression']

        input_variables = pd.DataFrame([[Country, Year, schizophrenia, bipolar, eating_disorder, anxiety, drug_use, depression]],
                                       columns=['Country', 'Year', 'schizophrenia', 'bipolar', 'eating_disorder',
                                                'anxiety', 'drug_use', 'depression'],
                                       index=['input'])

        # Encode country value
        l = LabelEncoder()
        input_variables['Country'] = l.fit_transform(input_variables['Country'])

        # Change data types of specific columns
        input_variables['Year'] = input_variables['Year'].astype(int)
        float_columns = ['schizophrenia', 'bipolar', 'eating_disorder', 'anxiety', 'drug_use', 'depression']
        input_variables[float_columns] = input_variables[float_columns].astype(float)

        predictions = model.predict(input_variables)[0]
        # print(predictions)

        # Plot graph
        data = pd.read_csv('data.csv')
        filtered_data = data[data['Entity'] == Country]
        new_row = {'Entity': Country, 'Year': Year, 'DALYs': predictions}
        filtered_data.loc[len(filtered_data)] = new_row

        fig = px.bar(filtered_data, x='Year', y='DALYs', color='Year', template='plotly_dark',  color_continuous_scale=px.colors.sequential.Blues)
        fig.update_xaxes(dtick=1)

        graph = fig.to_html(full_html=False)

        return flask.render_template('main.html',
                                     original_input={'Country': Country, 'Year': Year, 'schizophrenia': schizophrenia,
                                                     'bipolar': bipolar, 'eating_disorder': eating_disorder,
                                                     'anxiety': anxiety, 'drug_use': drug_use,
                                                     'depression': depression},
                                     result=predictions, graph=graph)

if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(debug=True)
