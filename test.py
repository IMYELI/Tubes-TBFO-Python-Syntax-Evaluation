def compressedSingleChannel(channelMatrix, rank):
    A = channelMatrix
    AT = np.transpose(channelMatrix)

    # Jika baris matriks lebih besar daripada kolom matriks, maka hitung ATA
    # Output berupa matriks singular dan matriks V, perlu ditranspose
    if (rowMatrix(channelMatrix) >= kolMatrix(channelMatrix)):
        ATA = np.matmul(AT,A,dtype)
        k = ATA.shape[0]
        E,V = simultaneous_power_iteration(ATA,k)
        E_full = np.sqrt(np.abs(np.diag(checkZerosinR(E))))
        VT = np.transpose(V)
        EVT = np.matmul(E_full,VT,dtype)
        EVT_inverse = np.linalg.inv(EVT)
        U = np.matmul(channelMatrix,EVT_inverse,dtype)

    # Jika baris matriks lebih kecil daripada kolom matriks, maka hitung AAT
    # Output berupa matriks singular dan matriks U
    elif (rowMatrix(channelMatrix) < kolMatrix(channelMatrix)):
        AAT = np.matmul(A,AT,dtype)
        k = AAT.shape[1]
        E = simultaneous_power_iteration(AAT,k)
        E_full = np.sqrt(np.abs(np.diag(checkZerosinR(E))))
        UE = np.matmul(U,E_full,dtype)
        UE_inverse = np.linalg.inv(UE)
        VT = np.matmul(UE_inverse,channelMatrix,dtype)

    aChannelCompressed = np.zeros((channelMatrix.shape[0],channelMatrix.shape[1]))
    k = rank
    aChannelCompressed = np.clip(aChannelCompressedInner,0,255)
    return aChannelCompressed