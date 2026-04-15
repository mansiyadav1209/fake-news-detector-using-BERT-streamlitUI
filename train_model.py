import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from torch.utils.data import Dataset

# Load dataset
df = pd.read_csv("fake_news.csv")

# Balanced sampling (1500 fake + 1500 real)
fake = df[df['label'] == 'FAKE'].sample(1500, random_state=42)
real = df[df['label'] == 'REAL'].sample(1500, random_state=42)

df = pd.concat([fake, real])

# Convert label to numbers
df['label'] = df['label'].map({'FAKE': 0, 'REAL': 1})

# Check balance
print(df['label'].value_counts())

# Combine title + text
texts = (df['title'] + " " + df['text']).tolist()

# Split dataset
train_texts, val_texts, train_labels, val_labels = train_test_split(
    texts,
    df['label'].tolist(),
    test_size=0.1,
    random_state=42
)

# Load tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Dataset class
class FakeDataset(Dataset):
    def __init__(self, texts, labels):
        self.encodings = tokenizer(texts, truncation=True, padding=True, max_length=512)
        self.labels = labels

    def __getitem__(self, idx):
        item = {k: torch.tensor(v[idx]) for k, v in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

# Create datasets
train_dataset = FakeDataset(train_texts, train_labels)
val_dataset = FakeDataset(val_texts, val_labels)

# Load model
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Training settings
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    logging_steps=50,
    save_strategy="no"
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset
)

# Train model
trainer.train()

# Save model
model.save_pretrained("fake_news_bert")
tokenizer.save_pretrained("fake_news_bert")

print("Model saved successfully!")