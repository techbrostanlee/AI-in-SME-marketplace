from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_cart_recommendations(cart_items):
    all_products = Product.query.all()
    product_texts = [
        (p.name or "") + " " + (p.category or "") + " " + (p.description or "")
        for p in all_products
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(product_texts)
    purchased_product_ids = [p["id"] for p in cart_items]
    purchased_indices = [i for i, p in enumerate(all_products) if p.id in purchased_product_ids]
    if not purchased_indices:
        return []
    user_vector = tfidf_matrix[purchased_indices].mean(axis=0)
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()
    recommended_indices = [
        i for i in similarity_scores.argsort()[::-1] if all_products[i].id not in purchased_product_ids
    ][:5]
    recommended_products = [all_products[i] for i in recommended_indices]
    return recommended_products


def analyze_amazon_sales_dataset(file_path):
    df = pd.read_csv(file_path)

    pd.set_option('display.max_columns', None)

    df['discounted_price'] = df['discounted_price'].str.replace("₹", '').str.replace(",", '').astype('float64')
    df['actual_price'] = df['actual_price'].str.replace("₹", '').str.replace(",", '').astype('float64')
    df['discount_percentage'] = df['discount_percentage'].str.replace('%', '').astype('float64') / 100

    df['rating'] = df['rating'].str.replace('|', '3.9').astype('float64')
    df['rating_count'] = df['rating_count'].str.replace(',', '').astype('float64')

    df['rating_count'] = df.rating_count.fillna(value=df['rating_count'].median())

    plt.figure(figsize=(22, 10))
    sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')

    plt.figure(figsize=(22, 10))
    missing_percentage = df.isnull().sum()/len(df)*100
    missing_percentage.plot(kind='bar')
    plt.xlabel('Columns')
    plt.ylabel('Percentage')
    plt.title('Percentage of Missing Values in each Column')

    plt.scatter(df['actual_price'], df['rating'])
    plt.xlabel('Actual_price')
    plt.ylabel('Rating')
    plt.show()

    plt.hist(df['actual_price'])
    plt.xlabel('Actual Price')
    plt.ylabel('Frequency')
    plt.show()

    encoders = {
        'product_id': LabelEncoder(),
        'category': LabelEncoder(),
        'review_id': LabelEncoder(),
        'review_content': LabelEncoder(),
        'product_name': LabelEncoder(),
        'user_name': LabelEncoder(),
        'about_product': LabelEncoder(),
        'user_id': LabelEncoder(),
        'review_title': LabelEncoder(),
        'img_link': LabelEncoder(),
        'product_link': LabelEncoder()
    }

    for col, encoder in encoders.items():
        df[col] = encoder.fit_transform(df[col])

    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True)
    plt.show()

    spearman_correlation_matrix = df.corr(method="spearman")
    sns.heatmap(spearman_correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix (Spearman)")
    plt.show()

    correlation_coefficient = np.corrcoef(df['actual_price'], df['rating'])[0, 1]

    grouped_df = df.groupby('category')['rating'].mean()

    std_price_by_brand = df.groupby('product_name')['actual_price'].std()

    pivot_table_1 = df.pivot_table(values='rating', index='category', columns='product_link', aggfunc='mean')
    pivot_table_2 = df.pivot_table(values='rating_count', index='review_content', columns='category', aggfunc='mean')

    t_statistic, p_value = stats.ttest_ind(
        df[df['category'] == 'electronics']['rating'],
        df[df['category'] == 'clothing']['rating']
    )

    contigency_table = pd.crosstab(df['actual_price'], df['rating'])
    chi2, p, dof, expected = stats.chi2_contingency(contigency_table)

    for col, encoder in encoders.items():
        df[col] = encoder.inverse_transform(df[col])

    return {
        "correlation": correlation_coefficient,
        "grouped_rating": grouped_df,
        "std_price_by_brand": std_price_by_brand,
        "pivot_rating_by_category_product_link": pivot_table_1,
        "pivot_ratingcount_by_review_category": pivot_table_2,
        "t_test": (t_statistic, p_value),
        "chi_square": (chi2, p, dof, expected)
    }
