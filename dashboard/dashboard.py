import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Set style untuk seaborn
sns.set(style='dark')

# Load data
all_df = pd.read_csv("./all_data.csv")

# Mengubah kolom 'dteday' menjadi format datetime
all_df["dteday"] = pd.to_datetime(all_df["dteday"])

# Filter data
min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

with st.sidebar:
    # Mengambil rentang waktu dari pengguna
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["dteday"] >= str(start_date)) & (all_df["dteday"] <= str(end_date))]

# Menampilkan informasi awal
st.header('Analisis Penyewaan Sepeda :bicyclist:')
st.write("Data ini menganalisis penyewaan sepeda berdasarkan suhu dan hari kerja.")

# Hubungan antara Suhu dan Jumlah Penyewaan Sepeda
st.subheader("Hubungan antara Suhu dan Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=all_df, x='dteday', y='cnt', label='Jumlah Penyewaan Sepeda', ax=ax, color='blue')
sns.lineplot(data=all_df, x='dteday', y='temp', label='Suhu Rata-Rata', ax=ax, color='orange')
ax.set_ylabel('Jumlah Penyewaan / Suhu')
ax.set_xlabel('Tanggal')
ax.set_title('Jumlah Penyewaan Sepeda vs Suhu Rata-Rata')
ax.legend()
st.pyplot(fig)

# Tabel hubungan suhu dan penyewaan
st.subheader("Tabel Hubungan Suhu dan Penyewaan Sepeda")
st.dataframe(all_df[['dteday', 'cnt', 'temp']].head(10))

# Pengaruh Hari Kerja
st.subheader("Pengaruh Hari Kerja Terhadap Total Penyewaan Sepeda")
working_day_counts = all_df.groupby('workingday')['cnt'].sum().reset_index()
working_day_counts['workingday'] = working_day_counts['workingday'].map({0: 'Tidak Bekerja', 1: 'Hari Kerja'})
fig, ax = plt.subplots(figsize=(7, 5))
sns.barplot(data=working_day_counts, x='workingday', y='cnt', palette='viridis', ax=ax)
ax.set_ylabel('Jumlah Penyewaan Sepeda')
ax.set_xlabel('Tipe Hari')
ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Tipe Hari')
st.pyplot(fig)

# Rata-rata penyewaan sepeda berdasarkan hari kerja
average_workingday = main_df.groupby("workingday")["cnt"].mean()
st.write("Rata-rata penyewaan sepeda:")
st.write(f"Pada hari kerja: {average_workingday[1]:.2f} sepeda")
st.write(f"Pada akhir pekan dan hari libur: {average_workingday[0]:.2f} sepeda")

# Tabel pengaruh hari kerja
st.subheader("Tabel Jumlah Penyewaan Sepeda Berdasarkan Tipe Hari")
st.dataframe(working_day_counts)

# Analisis 4: Histogram jumlah penyewaan
st.subheader("Distribusi Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(all_df['cnt'], bins=30, kde=True, ax=ax)
ax.set_xlabel('Jumlah Penyewaan Sepeda')
ax.set_ylabel('Frekuensi')
ax.set_title('Distribusi Jumlah Penyewaan Sepeda')
st.pyplot(fig)

# Analisis 5: Tren Bulanan
all_df['month'] = all_df['dteday'].dt.month
monthly_trend = all_df.groupby('month')['cnt'].sum().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=monthly_trend, x='month', y='cnt', palette='plasma', ax=ax)
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
ax.set_title('Tren Penyewaan Sepeda Bulanan')
st.pyplot(fig)

# Analisis 6: Tren Musiman
st.subheader("Tren Musiman Penyewaan Sepeda")
all_df['season'] = pd.cut(all_df['dteday'].dt.month, bins=[0, 3, 6, 9, 12], labels=['4', '1', '2', '3'], right=False)
seasonal_trend = all_df.groupby('season')['cnt'].sum().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=seasonal_trend, x='season', y='cnt', palette='coolwarm', ax=ax)
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Musim')
st.pyplot(fig)

# Analisis 7: Korelasi antara variabel
st.subheader("Korelasi Antara Variabel")
correlation_matrix = all_df.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
ax.set_title('Matriks Korelasi')
st.pyplot(fig)

# Menampilkan kesimpulan
st.subheader("Kesimpulan")
st.write("""
1. Terdapat hubungan positif antara suhu dan jumlah penyewaan sepeda. Ketika suhu meningkat, jumlah penyewaan sepeda juga cenderung meningkat.
2. Hari kerja memiliki pengaruh yang signifikan terhadap total penyewaan sepeda. Jumlah penyewaan sepeda pada hari kerja lebih tinggi dibandingkan dengan hari libur.
3. Distribusi jumlah penyewaan sepeda cenderung mengikuti pola normal dengan beberapa outlier.
4. Jumlah penyewaan sepeda bervariasi berdasarkan bulan, dengan tren musiman yang terlihat, dimana musim semi dan panas cenderung lebih tinggi dibandingkan dengan musim dingin.
5. Analisis korelasi menunjukkan hubungan antara beberapa variabel, memberikan wawasan lebih dalam tentang faktor yang mempengaruhi penyewaan sepeda.
""")


st.caption('Copyright © Your Name 2024')
