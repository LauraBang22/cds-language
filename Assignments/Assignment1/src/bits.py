#Absolutely, your script can be broken down into smaller, more manageable functions for better readability and maintainability. Here's a breakdown with suggested functions:

**1. Define helper functions:**

- **`clean_text(text)`**: This function can take the raw text as input and perform the cleaning steps (removing HTML tags using regex).

```python
def clean_text(text):
  pattern = r"<.*?>"
  cleaned_text = re.sub(pattern, "", text)
  return cleaned_text
```

- **`count_pos(doc)`**: This function can take the spaCy document and calculate the counts for nouns, verbs, adjectives, and adverbs.

```python
def count_pos(doc):
  noun_count = 0
  verb_count = 0
  adj_count = 0
  adv_count = 0
  for token in doc:
    if token.pos_ == "NOUN":
      noun_count += 1
    elif token.pos_ == "VERB":
      verb_count += 1
    elif token.pos_ == "ADJ":
      adj_count += 1
    elif token.pos_ == "ADV":
      adv_count += 1
  return noun_count, verb_count, adj_count, adv_count
```

- **`calculate_relative_freq(doc, count_tuple)`**: This function can take the document and the count tuple from `count_pos` and calculate the relative frequencies.

```python
def calculate_relative_freq(doc, count_tuple):
  noun_count, verb_count, adj_count, adv_count = count_tuple
  relative_freq_noun = round((noun_count / len(doc)) * 10000, 2)
  relative_freq_verb = round((verb_count / len(doc)) * 10000, 2)
  relative_freq_adj = round((adj_count / len(doc)) * 10000, 2)
  relative_freq_adv = round((adv_count / len(doc)) * 10000, 2)
  return relative_freq_noun, relative_freq_verb, relative_freq_adj, relative_freq_adv
```

- **`extract_named_entities(doc)`**: This function can take the document and extract the counts of unique named entities.

```python
def extract_named_entities(doc):
  persons = set()
  organisations = set()
  locations = set()
  for ent in doc.ents:
    if ent.label_ == 'PERSON':
      persons.add(ent.text)
    elif ent.label_ == 'ORG':
      organisations.add(ent.text)
    elif ent.label_ == 'LOC':
      locations.add(ent.text)
  return len(persons), len(organisations), len(locations)
```

- **`create_dataframe(folder_info)`**: This function can take the list of file information and create the pandas DataFrame.

```python
def create_dataframe(folder_info):
  df = pd.DataFrame(folder_info, 
                    columns=["Filename", "RelFreq NOUN", "RelFreq VERB", "RelFreq ADJ", "RelFreq ADV", 
                             "Unique PER", "Unique LOC", "Unique ORG"])
  return df
```

**2. Refactored `data_processing` function:**

```python
def data_processing(nlp):
  main_folder_path = ("in/USEcorpus")
  sorted_dir = sorted(os.listdir(main_folder_path))

  for folder in sorted_dir:
    folder_path = os.path.join(main_folder_path, folder)
    filenames = sorted(os.listdir(folder_path))
    folder_info = []

    for filename in filenames:
      filepath = folder_path + "/" + filename

      with open(filepath, encoding="latin-1") as f:
        text = f.read()

      cleaned_text = clean_text(text)
      doc = nlp(cleaned_text)

      noun_count, verb_count, adj_count, adv_count = count_pos(doc)
      relative_freq_noun, relative_freq_verb, relative_freq_adj, relative_freq_adv = calculate_relative_freq(doc, (noun_count, verb_count, adj_count, adv_count))
      num_persons, num_organisations,