import './Button.css';

export enum Colors {
    Primary = "primary",
    Secondary = "secondary",
    Accent = "accent"
}

export type ButtonProps = {
    circular?: boolean,
    color?: Colors,
    customColor?: string,
    large?: boolean,
    outline?: boolean,
    onClick?: () => void
}

export const Button: React.FC<ButtonProps> = ({ 
    circular = false,
    color = Colors.Primary,
    large = false,
    outline = false,
    customColor,
    onClick,
    children 
}) => {
    const buttonClass = ['button', color];

    if (circular)
        buttonClass.push('circular');

    if (large)
        buttonClass.push('large');

    if (outline)
        buttonClass.push('outline');

    return <button
        className={buttonClass.join(' ')}
        onClick={onClick}
        style={{ backgroundColor: customColor }}
    >{children}</button>
}
