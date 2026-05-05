from statsmodels.stats.proportion import proportions_ztest

def ab_test_channel(df):
    ab_data = df[df['CampaignChannel'].isin(['Email','Social'])]

    email = ab_data[ab_data['CampaignChannel']=='Email']['Conversion']
    social = ab_data[ab_data['CampaignChannel']=='Social']['Conversion']

    success = [email.sum(), social.sum()]
    total = [email.count(), social.count()]

    return proportions_ztest(success, total)


def ab_test_campaign_type(df):
    ab_data = df[df['CampaignType'].isin(['Conversion','Awareness'])]

    groupA = ab_data[ab_data['CampaignType']=='Conversion']['Conversion']
    groupB = ab_data[ab_data['CampaignType']=='Awareness']['Conversion']

    success = [groupA.sum(), groupB.sum()]
    total = [groupA.count(), groupB.count()]

    return proportions_ztest(success, total)