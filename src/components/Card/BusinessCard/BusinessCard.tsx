export type BusinessCardProps = {
    isSender: boolean,
    name: string,
    gst: string,
    address: string,
    phone: number
};

export const BusinessCard : React.FC<BusinessCardProps> = ({
    isSender = false,
    name = 'NA',
    gst = 'NA',
    address = 'NA',
    phone = 123
}) => <div className="BusinessCard">
    <h5>{isSender ? 'Sender' : 'Receiver'}</h5>
    <h1>{name}</h1>
    <h2>{gst}</h2>
    <p>{address}</p>
    <p>Phone: {phone}</p>
</div>