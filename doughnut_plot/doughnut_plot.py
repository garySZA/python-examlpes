import matplotlib.pyplot as plt

def create_doughnut( labels , sizes, explode ):
    fig, ax = plt.subplots()
    ax.pie( sizes, explode = explode, labels = labels, autopct = '%1.1f%%', startangle=90, shadow=True, colors=plt.cm.tab20.colors )
    ax.axis('equal')

    center_circle = plt.Circle((0, 0), 0.7, color='white', fc='white', linewidth=1.25)
    fig.gca().add_artist(center_circle)

    plt.title('Doughnut example')

    plt.show()

labels = ['Apples', 'Oranges', 'Bananas', 'Cherries']
sizes = [20, 30, 40, 10]
explode = (0, 0, 0, 0.1)

create_doughnut( labels, sizes, explode )
