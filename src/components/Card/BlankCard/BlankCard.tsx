import './BlankCard.scss'

export type BlankCardProps = {
    className: any;
    children: any;
}

export const BlankCard: React.FC<BlankCardProps> = ({
    className,
    children
}) => {
    return <div className={`BlankCard ${className}`}>
        {children}
    </div>
}