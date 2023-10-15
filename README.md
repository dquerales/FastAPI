# FastApi

*This is an example to deploy a model using FastApi*

## Installation

1. Install requirements
```
pip install -r "requirements.txt"
```
2. Run train model
```
cd 'path'
```
```
python src/train_model.py
```

## Usage

1. Run FastApi local host
```
python -m uvicorn api:app --reload
```
2. Open POSTMAN and test this request:

```  
{
    "sepal_length":6.5,
    "sepal_width":3.0,
    "petal_length":5.5,
    "petal_width":1.8
}
```

3. The output should be the following prediction:

```  
{
    "prediction": "['virginica']"
}
```

# Contact

Daniel Querales - d.querales@gmail.com

