import './SimpleCard.css'

export type SimpleCardProps = {
    header: string,
    description: string,
    actionLabel: string,
    actionLink: string,
}

export const SimpleCard: React.FC<SimpleCardProps> = ({
    header,
    description,
    actionLabel,
    actionLink
}) => {
    return <div className="SimpleCard">
        <h1>{header}</h1>
        <p>{description}</p>
        <div className="actions">
            <a href={actionLink}>{actionLabel}</a>
        </div>
    </div>
}