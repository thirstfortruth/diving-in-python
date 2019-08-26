import json

def to_json(func):
    def convert(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return convert


@to_json
def get_data():
  return {
    'data': 42
  }
  
print(get_data())# вернёт '{"data": 42}'

