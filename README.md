# Project Documentation

## 1. Corpus Composition

This corpus consists of 4 English translations of guiding cases from Mainland China.

- **Source**: PKULAW
- **Files and Word Counts**:
  - `guiding_case_no_215_en`: 9,778 words
  - `guiding_case_no_217_en`: 13,908 words
  - `guiding_case_no_224_en`: 5,422 words
  - `guiding_case_no_229_en`: 3,649 words
  - total: 32,757 words

## 2. Batch Rename of DOC Files — Python Script

**Example**:
- **Original Title**: *Guiding Case No. 215: People v. Kunming Min [REDACTED] Paper Co., Ltd. et al. (case of civil public interest litigation... (FBM-CLI.C.546010142(EN))*
- **Renamed as**: `guiding_case_no_215_en`

## 3. Batch Convert DOC Files to TXT Format — Python Script

## 4. Batch Clean TXT Files — Python Script

## 5. Batch Clean TXT Files — EmEditor "Batch Replace Text" Function

- **EmEditor Regular Expressions Based on Perl Language**

**Instructions**:
1. Fill in the search-and-replace fields on the left panel.
2. Check the "Regular Expressions" and "Search All Open Documents" options.
3. Add each step to the batch.
4. Steps will appear on the right panel; double-click to edit if needed.
5. After editing, save changes to the batch. Use `Ctrl + Z` to undo and test any new expressions.
6. Export the batch for reuse.

## 6. Multi-Dimensional Analysis Tool (MAT)

- **Tag Function**:
  - Texts tagged with Stanford will appear in folders named `ST_name_of_folder` or `ST_name_of_file`.
  - Texts tagged with MAT will appear in folders named `MAT_name_of_folder` or `MAT_name_of_text`.

- **Analyze Function**:
  - Generates a "Statistics" folder, including comparison charts and statistical data that contrast the linguistic features across 6 dimensions for Mainland China's leading cases and Biber's oral and written genres.

## 7. Preliminary Results of MAT_output

**Dimension 1 - Involvement vs. Informational**
- **Result**:The MAT output for leading cases in mainland China has the lowest score, with a negative value, closely aligning it with official documents.

**Dimension 2 - Narrative vs. Non-Narrative**
- **Result**: MAT_output scores negatively, close to the style of conversations.

**Dimension 3 - Explicit vs. Situation-Dependent Reference**
- **Result**: MAT_output ranks the highest with a positive score, similar to official documents.

**Dimension 4 - Expression of Persuasion**
- **Result**: MAT_output scores negatively, similar to press reportage.

**Dimension 5 - Abstract vs. Non-Abstract Information**
- **Result**: MAT_output scores positively, resembling press reportage.

**Dimension 6 - On-Line Informational Elaboration**
- **Result**: MAT_output scores negatively, aligning closely with official documents.
