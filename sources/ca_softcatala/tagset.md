# Tagset for Catalan (ca)

Following tagset is highly derived from [Freeling project](https://freeling-user-manual.readthedocs.io/en/latest/tagsets/tagset-ca/#part-of-speech-verb).

### Part of Speech: `adjective`

| Position | Atribute      | Values                                                     |
|:---------|:--------------|:-----------------------------------------------------------|
| 0        | category      | **A**:*adjective*                                          |
| 1        | type          | **O**:*ordinal*; **Q**:*qualificative*; **P**:*possessive* |
| 2        | degree        | **S**:*superlative*; **V**:*evaluative*                    |
| 3        | gender        | **F**:*feminine*; **M**:*masculine*; **C**:*common*        |
| 4        | number        | **S**:*singular*; **P**:*plural*; **N**:*invariable*       |
| 5        | possessorpers | **1**:*1*; **2**:*2*; **3**:*3*                            |
| 6        | possessornum  | **S**:*singular*; **P**:*plural*; **N**:*invariable*       |

### Part of Speech: `conjunction`

| Position | Atribute | Values                                      |
|:---------|:---------|:--------------------------------------------|
| 0        | category | **C**:*conjunction*                         |
| 1        | type     | **C**:*coordinating*; **S**:*subordinating* |

### Part of Speech: `determiner`

| Position | Atribute     | Values                                                                                                                                       |
|:---------|:-------------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| 0        | category     | **D**:*determiner*                                                                                                                           |
| 1        | type         | **A**:*article*; **D**:*demonstrative*; **I**:*indefinite*; **P**:*possessive*; **R**:*relative*; **T**:*interrogative*; **E**:*exclamative* |
| 2        | person       | **1**:*1*; **2**:*2*; **3**:*3*                                                                                                              |
| 3        | gender       | **F**:*feminine*; **M**:*masculine*; **C**:*common*                                                                                          |
| 4        | number       | **S**:*singular*; **P**:*plural*; **N**:*invariable*                                                                                         |
| 5        | possessornum | **S**:*singular*; **P**:*plural*; **N**:*invariable*                                                                                         |

### Part of Speech: `noun`

| Position | Atribute   | Values                                                                |
|:---------|:-----------|:----------------------------------------------------------------------|
| 0        | category   | **N**:*noun*                                                          |
| 1        | type       | **C**:*common*; **P**:*proper*                                        |
| 2        | gender     | **F**:*feminine*; **M**:*masculine*; **C**:*common*                   |
| 3        | number     | **S**:*singular*; **P**:*plural*; **N**:*invariable*                  |
| 4        | neclass    | **S**:*person*; **G**:*location*; **O**:*organization*; **V**:*other* |
| 5        | nesubclass | *Not used*                                                            |
| 6        | degree     | **V**:*evaluative*                                                    |

### Part of Speech: `pronoun`

| Position | Atribute | Values                                                                                                                    |
|:---------|:---------|:--------------------------------------------------------------------------------------------------------------------------|
| 0        | category | **P**:*pronoun*                                                                                                           |
| 1        | type     | **D**:*demonstrative*; **E**:*exclamative*; **I**:*indefinite*; **P**:*personal*; **R**:*relative*; **T**:*interrogative* |
| 2        | person   | **1**:*1*; **2**:*2*; **3**:*3*                                                                                           |
| 3        | gender   | **F**:*feminine*; **M**:*masculine*; **C**:*common*                                                                       |
| 4        | number   | **S**:*singular*; **P**:*plural*; **N**:*invariable*                                                                      |
| 5        | case     | **N**:*nominative*; **A**:*accusative*; **D**:*dative*; **O**:*oblique*                                                   |
| 6        | polite   | **P**:*yes*                                                                                                               |

### Part of Speech: `adverb`

| Position | Atribute | Values                            |
|:---------|:---------|:----------------------------------|
| 0        | category | **R**:*adverb*                    |
| 1        | type     | **N**:*negative*; **G**:*general* |

### Part of Speech: `adposition`

| Position | Atribute | Values              |
|:---------|:---------|:--------------------|
| 0        | category | **S**:*adposition*  |
| 1        | type     | **P**:*preposition* |

### Part of Speech: `verb`

| Position | Atribute | Values                                                                                                              |
|:---------|:---------|:--------------------------------------------------------------------------------------------------------------------|
| 0        | category | **V**:*verb*                                                                                                        |
| 1        | type     | **M**:*main*; **A**:*auxiliary*; **S**:*semiauxiliary*                                                              |
| 2        | mood     | **I**:*indicative*; **S**:*subjunctive*; **M**:*imperative*; **P**:*participle*; **G**:*gerund*; **N**:*infinitive* |
| 3        | tense    | **P**:*present*; **I**:*imperfect*; **F**:*future*; **S**:*past*; **C**:*conditional*                               |
| 4        | person   | **1**:*1*; **2**:*2*; **3**:*3*                                                                                     |
| 5        | number   | **S**:*singular*; **P**:*plural*                                                                                    |
| 6        | gender   | **F**:*feminine*; **M**:*masculine*; **C**:*common*; **N**:*neuter*                                                 |
| 7        | variant  | **0**:*general*; **1**:*subjuntive_alt1*; **2**:*subjuntive_alt2*; **3**:*subjuntive_alt3*; **4**:*subjuntive_alt4*; **5**:*subjuntive_alt5*; **6**:*subjuntive_alt6*; **7**:*subjuntive_alt7*; **B**:*balear*; **C**:*central*; **F**:*old_fossil*; **N**:*northern*; **V**:*valencian*; **W**:*north-western*; **X**:*central_and_valencian*; **Y**:*central_and_balear*; **Z**:*balear_and_valencian* |

### Part of Speech: `number`

| Position | Atribute | Values                                                                |
|:---------|:---------|:----------------------------------------------------------------------|
| 0        | category | **Z**:*number*                                                        |
| 1        | type     | **d**:*partitive*; **m**:*currency*; **p**:*percentage*; **u**:*unit* |

### Part of Speech: `date`

| Position | Atribute | Values       |
|:---------|:---------|:-------------|
| 0        | category | **W**:*date* |

### Part of Speech: `interjection`

| Position | Atribute | Values               |
|:---------|:---------|:---------------------|
| 0        | category | **I**:*interjection* |

## Non-positional tags

### Part of Speech: `punctuation`

| Tag | Attributes                                                                  |
|:----|:----------------------------------------------------------------------------|
| Fd  | **pos**:*punctuation*; **type**:*colon*                                     |
| Fc  | **pos**:*punctuation*; **type**:*comma*                                     |
| Flt | **pos**:*punctuation*; **type**:*curlybracket*; **punctenclose**:*close*    |
| Fla | **pos**:*punctuation*; **type**:*curlybracket*; **punctenclose**:*open*     |
| Fs  | **pos**:*punctuation*; **type**:*etc*                                       |
| Fat | **pos**:*punctuation*; **type**:*exclamationmark*; **punctenclose**:*close* |
| Faa | **pos**:*punctuation*; **type**:*exclamationmark*; **punctenclose**:*open*  |
| Fg  | **pos**:*punctuation*; **type**:*hyphen*                                    |
| Fz  | **pos**:*punctuation*; **type**:*other*                                     |
| Fpt | **pos**:*punctuation*; **type**:*parenthesis*; **punctenclose**:*close*     |
| Fpa | **pos**:*punctuation*; **type**:*parenthesis*; **punctenclose**:*open*      |
| Ft  | **pos**:*punctuation*; **type**:*percentage*                                |
| Fp  | **pos**:*punctuation*; **type**:*period*                                    |
| Fit | **pos**:*punctuation*; **type**:*questionmark*; **punctenclose**:*close*    |
| Fia | **pos**:*punctuation*; **type**:*questionmark*; **punctenclose**:*open*     |
| Fe  | **pos**:*punctuation*; **type**:*quotation*                                 |
| Frc | **pos**:*punctuation*; **type**:*quotation*; **punctenclose**:*close*       |
| Fra | **pos**:*punctuation*; **type**:*quotation*; **punctenclose**:*open*        |
| Fx  | **pos**:*punctuation*; **type**:*semicolon*                                 |
| Fh  | **pos**:*punctuation*; **type**:*slash*                                     |
| Fct | **pos**:*punctuation*; **type**:*squarebracket*; **punctenclose**:*close*   |
| Fca | **pos**:*punctuation*; **type**:*squarebracket*; **punctenclose**:*open*    |
