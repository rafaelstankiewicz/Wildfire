import matplotlib.pyplot as plt

train_loss = [0.65, 0.2830, 0.2205, 0.2003, 0.1917, 0.1774, 0.1680, 0.1580, 0.1541, 0.1457, 0.1440] # Placeholder value for epoch 10 training loss
val_loss = [0.65, 0.2217, 0.1799, 0.1725, 0.1532, 0.1486, 0.1387, 0.1562, 0.1295, 0.1716, 0.1251] # Placeholder value for epoch 10 validation loss

plt.figure(figsize=(8, 5)) 

plt.plot(train_loss, label='CNN Train Loss')
plt.plot(val_loss, label='CNN Valid Loss')

train_loss_model2 = [0.65, 0.46, 0.42, 0.41, 0.40, 0.40, 0.39, 0.39, 0.39, 0.39, 0.38]
val_loss_model2 = [0.65, 0.40, 0.40, 0.39, 0.38, 0.38, 0.37, 0.42, 0.38, 0.39, 0.37]

plt.plot(train_loss_model2, label='ViT Train Loss', color='green')
plt.plot(val_loss_model2, label='ViT Valid Loss', color='red')

plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss Comparison for CNN and ViT')

plt.legend()

plt.ylim(min(train_loss + val_loss + train_loss_model2 + val_loss_model2) - 0.01, max(train_loss + val_loss + train_loss_model2 + val_loss_model2) + 0.01)

plt.xlim(0, 10)  

plt.grid(True)
plt.show()