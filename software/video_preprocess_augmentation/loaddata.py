def loaddata(Video_dir,n_classes):
    files = os.listdir(Video_dir)
    X = []
    labels = []
    
    for i in range(n_classes):
        path = os.path.join(Video_dir, 'c'+str(i),'*.avi')
        files = glob.glob(path)
      
        for filename in files:
            labels.append(i)
            X.append(load_video(filename))
return np.array(X) , np.array(labels)