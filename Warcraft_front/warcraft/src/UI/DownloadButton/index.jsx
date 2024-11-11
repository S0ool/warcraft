
export const DownloadButton = ({
                                   url = 'https://us.battle.net/support/en/article/256212',
                                   title = 'Скачать официальный Warcraft 3'
                               }) => {
    return (
        <button onClick={() => window.location.href = url} className="downloadButton">{title}</button>
    )
}