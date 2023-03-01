import cv2

img = cv2.imread("C:/Users/Juinior/Desktop/Maria/Projeto104/solar-system.jpg") 


cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )

cv2.putText(img,
            "Mercurio",
            (100,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0)
            )

cv2.putText(img,
            "Venus",
            (190,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0)
            )

cv2.putText(img,
            "Terra",
            (280,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0)
            )

cv2.putText(img,
            "Marte",
            (370,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0)
            )

cv2.putText(img,
            "Jupiter",
            (460,80),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0)
            )

cv2.putText(img,
            "Saturno",
            (750,295),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0)
            )

cv2.putText(img,
            "Urano",
            (970,295),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0)
            )


cv2.putText(img,
            "Netuno",
            (1100,295),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,0)
            )

cv2.imshow("resultado", img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)