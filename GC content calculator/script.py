from Bio import SeqIO
import matplotlib.pyplot as plt
import csv

# Read DNA Sequence from FASTA file

# Seqio.read is used when the file contains a single sequence. for multiple sequences, you'd use SeqIO.parse
record = SeqIO.read("C:/Users/user/Downloads/sequence (3).fasta", "fasta")
sequence = str(record.seq)

# GC content calculation

def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return gc / len(seq)

# Sliding window

window_size = 100
gc_values = []

for i in range(0, len(sequence) - window_size + 1):
    window = sequence[i:i+window_size]
    gc_values.append(gc_content(window))

# plot
plt.plot(gc_values)
plt.xlabel("Window Position")
plt.ylabel("GC Content")
plt.title("Sliding Window GC content from FASTA")
plt.grid(True)


# Adding colour band

for i, gc in enumerate(gc_values):
    color = (
        "green" if gc > 0.6 else
        "red" if gc < 0.4 else
        "orange"
    )
    plt.axvspan(i, i+1, color=color, alpha=0.5)
plt.plot(gc_values, color = "black")
plt.show()

with open("gc_content_output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Start", "End", "GC_Contet"])

    for i, gc in enumerate(gc_values):
        start = i
        end = i + window_size
        writer.writerow([start, end, gc])
        


