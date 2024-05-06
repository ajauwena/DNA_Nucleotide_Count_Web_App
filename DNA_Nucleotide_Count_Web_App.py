# Title: --- DNA Nucleotide Count Web App ---

# region: --- Importing Modules ---

import pandas as pd # For importing dataframes.
import streamlit as st # For the web app.
import altair as alt # For the graph.
from PIL import Image # For importing images.

# endregion

# region: --- Defining Functions ---

# Define a function that counts the frequency of each nucleotide.
def dna_nuc_counter(seq):
    dict_dna_nuc = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return dict_dna_nuc

# endregion

# region: --- Page Title ---

# Write the header section.
st.write('''
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of an input sequence.
***
''') # '"""' marks the start and end regions, "#" marks a header, and "***" shows a horizontal separation line.

# endregion

# region: --- Input Sequence ---

# Write the input prompt.
st.header('Enter Sequence')

# Write the default input sequence.
input_sequence = '> DNA query\nATGCACTGACTAGTCGATCACTAGCAGG\nGATCATTTAAAGCGGCCAACGTAC\nACGTAAGCCTAGCTAGCATCAGACTGATCAGTCGAG'

# Define the properties of the input text box.
sequence = st.text_area('Enter your sequence below.', input_sequence, height = 250)

# Process the input sequence for analysis.
sequence = sequence.splitlines() # Splits the input sequence by lines, creating a list consisting of each line as elements.
sequence = sequence[1:] # Subsets only the second element (i.e., index 1) of the list onward to exclude the sequence name (a variable retrieves its most current value).
sequence = ''.join(sequence) # Concatenates the list to a string.

# Write a horizontal separation line.
st.write('''
***
''')

# Write the input sequence.
st.header('Input Sequence')
st.write(sequence)

# Write a horizontal separation line.
st.write('''
***
''')

# endregion

# region: --- Output Sequence ---

# Write the output sequence.
st.header('DNA Nucleotide Count')
st.write('The DNA nucleotide count is displayed in different formats.')

# Display the DNA nucleotide count as a dictionary.
st.subheader('1. As a dictionary.')
dict_dna_nuc_count = dna_nuc_counter(sequence)
st.write(dict_dna_nuc_count)

# Display the DNA nucleotide count as a text.
st.subheader('2. As a text.')
st.write('There are ' + str(dict_dna_nuc_count['A']) + ' adenines (As).')
st.write('There are ' + str(dict_dna_nuc_count['T']) + ' thymines (Ts).')
st.write('There are ' + str(dict_dna_nuc_count['G']) + ' guanines (Gs).')
st.write('There are ' + str(dict_dna_nuc_count['C']) + ' cytosines (Cs).')

# Display the DNA nucleotide count as a DataFrame.
st.subheader('3. As a DataFrame.')
df_dna_nuc_count = pd.DataFrame.from_dict(dict_dna_nuc_count, orient = 'index') # "orient = "index"" uses the keys of the dictionary "dict_dna_nuc_count" as the indices (i.e., row labels) of the DataFrame.
df_dna_nuc_count = df_dna_nuc_count.rename({0: 'Count'}, axis = 'columns') # Renames the column name "0" to "count."
df_dna_nuc_count.reset_index(inplace = True) # Resets the DataFrame's indices (i.e., row labels) to start from "0," while the original indices are moved as row values in a new column.
df_dna_nuc_count = df_dna_nuc_count.rename(columns = {'index': 'Nucleotide'})
st.write(df_dna_nuc_count)

# Display the DNA nucleotide count as a bar chart.
st.subheader('4. As a bar chart.')
bar_chart = alt.Chart(df_dna_nuc_count).mark_bar().encode(
    x = 'Nucleotide',
    y = 'Count'
) # Creates a marked bar chart from the DataFrame "df_dna_nuc_count" and encodes the x- and y-axes with the labels "Nucleotide" and "Count," respectively.
bar_chart = bar_chart.properties(
    width = alt.Step(75)
)
st.write(bar_chart)

# Write a horizontal separation line.
st.write('''
***
''')

# endregion

# region: --- References ---

# Nantasenamat, C. [Data Professor]. (2020, September 30). How to build a simple bioinformatics web app in Python | Streamlit #8 [Video]. YouTube. https://www.youtube.com/watch?v=DD9tgg8ivbU

# endregion