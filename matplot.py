import numpy as np
import matplotlib.pyplot as plt

#sample data
accuracy_pre = {"Random Forest": 1, "Logistic Regression": 2, "KNN": 3}
accuracy_post = {"Random Forest": 4, "Logistic Regression": 5, "KNN": 6}

X = np.arange(len(accuracy_pre))
ax = plt.subplot(111)
ax.bar(X, accuracy_pre.values(), width=0.2, color='b', align='center')
ax.bar(X-0.2, accuracy_post.values(), width=0.2, color='g', align='center')
ax.legend(('Pre Accuracy','Post Accuracy'))
plt.xticks(X, accuracy_pre.keys())
plt.title("Accuracy score", fontsize=17)
plt.show()