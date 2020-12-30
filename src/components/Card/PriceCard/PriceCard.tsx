import './PriceCard.css'
import deleteSVG from '../../../assets/delete-black-18dp.svg';
import createSVG from '../../../assets/create-black-18dp.svg';

export type PriceCardProps = {
    description: string,
    itemType: string,
    quantity: number,
    price: number,
    removeAction: () => void,
    editAction: () => void
}

export const PriceCard: React.FC<PriceCardProps> = ({
    description,
    itemType,
    quantity,
    price,
    removeAction,
    editAction
}) => {
    return <div className="PriceCard">
        <div className="headerSection">
            <div className="description">
                <h1>{description}</h1>
                <p>{itemType}</p>
            </div>
            <div className="actions">
                <img src={deleteSVG} onClick={removeAction} />
                <img src={createSVG} onClick={editAction} />
            </div>
        </div>
        <div className="priceSection">
            <p className="quantity">Qty: {quantity}</p>
            <p className="price">₹  {price}</p>
        </div>
    </div>
}