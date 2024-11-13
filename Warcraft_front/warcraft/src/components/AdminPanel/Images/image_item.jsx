import styles from "./styles.module.css";
import {forwardRef} from "react";
import {Link} from "react-router-dom";

export const ImageItem = forwardRef(({image, is_admin, setImgModalOpen}, ref) => {
    return (
        <div className={styles.image} ref={ref}>
            <h3 className={styles.image_name}>
                <Link to={`/Admin/images/${image.id}`}>
                    {image.name || "Нет имени"}
                </Link>
            </h3>
            <img
                className={styles.image_img}
                src={image.image}
                alt={image.name}
                onClick={setImgModalOpen}
            />
            <p className={styles.image_description}>{image.description}</p>
        </div>
    );
});
