import seaborn as sns
import matplotlib.pyplot as plt

def plot_channel_conversion(df):
    sns.barplot(x='CampaignChannel', y='Conversion', data=df)
    plt.title("Conversion Rate by Campaign Channel")
    plt.show()


def plot_campaign_type(df):
    sns.barplot(x='CampaignType', y='Conversion', data=df)
    plt.title("Conversion Rate by Campaign Type")
    plt.show()


def plot_campaign_distribution(df):
    sns.countplot(x='CampaignType', data=df)
    plt.title("User Distribution Across Campaign Types")
    plt.show()