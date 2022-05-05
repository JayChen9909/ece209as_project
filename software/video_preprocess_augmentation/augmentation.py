def augmentation(X_train,Y_train):
    for i in range(no_of_samples):
        idx = random.randint(0,59)# 59 is no. of videos available for augmentation
        vid = X_train[idx]
        video_aug = np.array(seq(vid))
        X_train_aug.append(video_aug)
        Y_train_aug.append(Y_train[idx])
    return np.array(X_train_aug),np.array(Y_train_aug)