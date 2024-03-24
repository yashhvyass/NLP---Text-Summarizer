import os
from src.textSummarizer.entity import DataTransformationConfig
from src.textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length=128, truncation=True)

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def convert(self):
        # Load dataset from disk
        dataset_samsum = load_from_disk(self.config.data_path)

        # Reduce the size of train, test, and validation datasets
        train_data = dataset_samsum['train'].select(range(500))
        test_data = dataset_samsum['test'].select(range(250))
        valid_data = dataset_samsum['validation'].select(range(250))

        # Convert examples to features
        train_dataset = train_data.map(self.convert_examples_to_features, batched=True)
        test_dataset = test_data.map(self.convert_examples_to_features, batched=True)
        valid_dataset = valid_data.map(self.convert_examples_to_features, batched=True)

        # Create directories if they don't exist
        output_dir = os.path.join(self.config.root_dir, "samsum_dataset")
        os.makedirs(output_dir, exist_ok=True)

        # Save datasets to disk
        train_dataset.save_to_disk(os.path.join(output_dir, "train"))
        test_dataset.save_to_disk(os.path.join(output_dir, "test"))
        valid_dataset.save_to_disk(os.path.join(output_dir, "validation"))
