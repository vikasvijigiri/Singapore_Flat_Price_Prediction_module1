import os
import pickle
import pandas as pd
from django.shortcuts import render
from django.http import JsonResponse
import gdown

# # Load the model
# model_path = os.path.join(os.path.dirname(__file__), 'singapore_flat_1990_1999.pkl')
# with open(model_path, 'rb') as f:
#     model = pickle.load(f)

# encoder_path = os.path.join(os.path.dirname(__file__), 'singapore_flat_1990_1999_OrdEnc.pkl')
# with open(encoder_path, 'rb') as f:
#     encoder = pickle.load(f)



# Define the Google Drive file IDs for the model and encoder
model_file_id = '1kh4nAST-IWwenE_MaGCUR2lCFL5Y5LE7'
encoder_file_id = '1GW0-k5XoZNg4pKCXRL843PwcwRoYRlBB'

# Define the destination paths for the model and encoder files
model_path = 'model.pkl'
encoder_path = 'encoder.pkl'

# Download the model file from Google Drive
gdown.download(f'https://drive.google.com/uc?id={model_file_id}', model_path, quiet=False)

# Download the encoder file from Google Drive
gdown.download(f'https://drive.google.com/uc?id={encoder_file_id}', encoder_path, quiet=False)

# Load the model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Load the encoder
with open(encoder_path, 'rb') as f:
    encoder = pickle.load(f)



def transform_features(features, encoder):
    df = pd.DataFrame(columns=['block', 'street_name', 'storey_range', 'floor_area_sqm', 'flat_model', 'lease_commence_date', 	
                               'month_1', 'year_1'])

    # Ensure the features list has enough elements
    if len(features) < 7:
        raise ValueError("Insufficient number of elements in the features list.")

    # Parse the date and extract month and year
    df['month_1'] = [pd.to_datetime(features[0]).month]
    df['year_1'] = [pd.to_datetime(features[0]).year]

    # Assign the storey range and map it to the corresponding value
    df['storey_range'] = features[3]
    df['storey_range'] = df['storey_range'].map({
        '10 TO 12': 11, '04 TO 06': 5, '07 TO 09': 8, '01 TO 03': 2, '13 TO 15': 14,
        '19 TO 21': 20, '16 TO 18': 17, '25 TO 27': 26, '22 TO 24': 23
    })

    # Assign floor area and lease commence date
    df['floor_area_sqm'] = features[4]
    df['lease_commence_date'] = features[6]

    # Create a DataFrame for the categorical features
    category_to_encode = pd.DataFrame({
        'block': [features[1]],
        'street_name': [features[2]],
        'flat_model': [features[5]]
    })

    # Encode the categorical features
    encoded_categories = encoder.transform(category_to_encode)
    df[['block', 'street_name', 'flat_model']] = encoded_categories

    return df

    

def predict(request):
    if request.method == 'POST':
        data = request.POST
        # Extract features from request data
        features = [
            str(data.get('month')),
            str(data.get('block')),
            str(data.get('street_name')),
            str(data.get('storey_range')),
            float(data.get('floor_area_sqm')),
            str(data.get('flat_model')),
            int(data.get('lease_commence_date')),
        ]
        df = transform_features(features, encoder)

        #print(df)
        # Perform prediction
        prediction = model.predict(df)
        return JsonResponse({'Resale Price (predicted)': prediction[0].round(2)})
    return render(request, 'predict.html')