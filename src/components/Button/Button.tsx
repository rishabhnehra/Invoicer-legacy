import './Button.css';

export enum Colors {
    PRIMARY = "primary",
    SECONDARY = "secondary",
    ACCENT = "accent"
}

export type ButtonProps = {
    circular?: boolean,
    color?: Colors,
    customColor?: string,
    large?: boolean,
    outline?: boolean
    onClick?: () => void
}

export const Button: React.FC<ButtonProps> = ({ circular = false, color = Colors.PRIMARY, large = false, outline = false, onClick, children }) => {
    let buttonClass = `button ${color}`

    if (circular)
        buttonClass += ` circular`;

    if (large)
        buttonClass += ` large`;

    if (outline)
        buttonClass += ` outline`;

    return <button
        className={buttonClass}
        onClick={onClick}
    >{children}</button>
}
