from sklearn.datasets import load_iris
iris = load_iris()

iris_dict = dict([(i,v) for i,v in enumerate(iris['target_names']) ])
iris_names = [iris_dict[_] for _ in iris['target']]

iris_counts = dict([ (t, iris_names.count(t)) for t in iris['target_names'] ])

for k,v in iris_counts.items():
    print(f"{k.ljust(10)}: {'*'*v}")
