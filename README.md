
1. Corpus Composition
This corpus consists of 4 English leading cases from Mainland China, with a total of 32,757 words.

Source: PKULAW

Files and Word Counts：

guiding_case_no_215_en: 9,778 words

guiding_case_no_217_en: 13,908 words

guiding_case_no_224_en: 5,422 words

guiding_case_no_229_en: 3,649 words


2. Batch Rename of DOC Files — Python Script
   
Example:

Original Title: Guiding Case No. 215: People v. Kunming Min [REDACTED] Paper Co., Ltd. et al. (case of civil public interest litigation... (FBM-CLI.C.546010142(EN))

Renamed as: guiding_case_no_215_en

3. Batch Convert DOC Files to TXT Format — Python Script
   
4. Batch Clean TXT Files — Python Script
 
5. Batch Clean TXT Files — EmEditor "Batch Replace Text" Function
 
*EmEditor Regular Expressions Based on Perl Language

Instructions:
Fill in the search-and-replace fields on the left panel.
Check "Regular Expressions" and "Search All Open Documents" options.
Add each step to the batch.
Steps will appear on the right panel; double-click to edit if needed.
After editing, save changes to the batch. Use Ctrl + Z to undo and test any new expressions.
Export the batch for reuse.

6. Multi-Dimensional Analysis Tool (MAT)
   
Tag Function:
Texts tagged with Stanford will appear in folders named ST_name_of_folder or ST_name_of_file.
Texts tagged with MAT will appear in folders named MAT_name_of_folder or MAT_name_of_text.

Analyze Function:
Generates a "Statistics" folder, including comparison charts and statistical data that contrast the linguistic features across 6 dimensions for Mainland China's leading cases and Biber's oral and written genres.
