import styles from "./styles.module.css"

export const ImageItem = ({image}) => {
    return (
        <div className={styles.image}>
            <h3>{image.name}</h3>
            <img src={image.image} alt={image.name}/>
            <p>{image.description}</p>
        </div>
    )
}