def conversion_metrics(df):
    results = {}

    results['conversion_mean'] = df['Conversion'].mean()
    results['campaign_type'] = df.groupby('CampaignType')['Conversion'].mean()
    results['platform'] = df.groupby('AdvertisingPlatform')['Conversion'].mean()
    results['channel'] = df.groupby('CampaignChannel')['Conversion'].mean()
    results['landing_page'] = df.groupby('landing_page')['converted'].mean()
    results['group'] = df.groupby('group')['converted'].mean()

    return results


def conversion_rate_calc(df):
    df['conversion_rate'] = df['approved_conversion'] / df['clicks']
    return df[['clicks','approved_conversion','conversion_rate']]