import requests

def make_post(username, password, model_json , acc, val_acc, loss, val_loss, title, evaluate, report):
  data = {'username':username,
            'password':password}
  x = requests.post(('https://schwarzam.art/api/auth/login'), data=data, json={'Content-Type': 'application/json'}, verify=False)

  if x.status_code == 200:
    x = (x.json())
    token = x['token']
    username = x['user']['username']
    email = x['user']['email']

    jsnono = {'Content-Type': 'application/json'}
    headers = {'Authorization' : f'token {token}'}

    acc = str(list(acc))
    val_acc = str(list(val_acc))
    loss = str(list(loss))
    val_loss = str(list(val_loss))
    evaluate =f'{evaluate}'
    report = str(report.split('\n'))

    data = {'name': f'{username}',
            'email': f'{email}',
            'title': f'{title}',
            'model_json': model_json,
            'evaluate': evaluate,
            'report': report,
            'acc': (f'{(acc)}'),
            'val_acc': (f'{(val_acc)}'),
            'loss': (f'{(loss)}'),
            'val_loss': (f'{(val_loss)}')}

    response = requests.post('https://schwarzam.art/api/leadsML/', data=data, json=jsnono, headers=headers, verify=False)
    print(response.status_code ,'done')
  else:
      print('Failed!')

import time
from datetime import date

def save_drive(model , history, acc, val_acc, loss, val_loss):

  tempo = time.strftime("%H,%M")

  hoje = date.today()
  today1 = hoje.strftime("%B %d, %Y")
  today1 = today1.replace(" ", "")

  !mkdir '/content/drive/My Drive/TrainSets/Relatorios/'{today1}
  !mkdir '/content/drive/My Drive/TrainSets/Relatorios/'{today1}'/'{tempo}


  today = [today1 for i in loss]

  epochs = range(1, len(acc)+1)

  plot = plot_model(model, to_file=f"/content/drive/My Drive/TrainSets/Relatorios/{today1}/{tempo}/ModelUsed.jpg",
        show_shapes=True,
        show_layer_names=True,
        rankdir="TB",
        dpi=96,)

  plt.plot(epochs, loss, 'b', label='Training Loss')
  plt.plot(epochs, val_loss, 'r', label='Validation Loss')
  plt.title('Training and validation Loss')
  plt.legend()

  plt.savefig(f"/content/drive/My Drive/TrainSets/Relatorios/{today1}/{tempo}/Loss.jpg")
  plt.clf()

  plt.plot(epochs, acc, 'ko', label='Training acc')
  plt.plot(epochs, val_acc, 'k', label='Validation acc')
  plt.title('Training and validation accuracy')
  plt.legend()

  plt.savefig(f"/content/drive/My Drive/TrainSets/Relatorios/{today1}/{tempo}/Validation.jpg")
  plt.clf()

  model.save(f"/content/drive/My Drive/TrainSets/Relatorios/{today1}/{tempo}/Model")
